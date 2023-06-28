import cv2
import face_recognition
import numpy as np
import os
import pickle
import pymysql
from datetime import datetime, timedelta

"""
    [TODO] - Add feature to send logs first logged in of the day and
    after 10 minutes the next send logs will be sent as logged out then
    don't send logs for the next 10 minutes
"""


class FacialRecognitionWindow(object):
    def __init__(self) -> None:
        self.logs_sent = False
        self.existing_logs = False
        self.detect_face_time = 0
        self.count = 0

        # Configurable values
        self.logout_minutes = 2
        self.valid_face_accuracy_value = 0.5
        self.retries = 3

    def face_recognition_func(self):
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        # Importing student images
        folderModePath = "images"
        pathList = os.listdir(folderModePath)
        imgList = []
        studentIds = []
        for path in pathList:
            imgList.append(cv2.imread(os.path.join(folderModePath, path)))

        # Load the encoding file
        print("Loading Encoding File ....")
        file = open("FaceEncodeFile.p", "rb")
        encodeListKnownWithIds = pickle.load(file)
        file.close()
        encodeListKnown, studentIds = encodeListKnownWithIds
        print("Encoding File Loaded")

        cur_face = ""
        while True:
            try:
                ret, frame = cap.read()

                imgS = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
                imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

                faceCurFrame = face_recognition.face_locations(imgS)
                encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

                for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
                    matches = face_recognition.compare_faces(
                        encodeListKnown, encodeFace
                    )
                    faceDis = face_recognition.face_distance(
                        encodeListKnown, encodeFace
                    )

                    if any(faceDis <= self.valid_face_accuracy_value):
                        matchIndex = np.argmin(faceDis)

                        if matches[matchIndex]:
                            name = self.get_name_from_filename(
                                studentIds[matchIndex].upper()
                            )
                            y1, x2, y2, x1 = faceLoc
                            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                            cv2.putText(
                                frame,
                                name,
                                (x1 + 6, y2 + 25),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                0.60,
                                (255, 255, 255),
                                2,
                            )
                        self.detect_face_time += 1
                        print(self.logs_sent)
                        print(self.detect_face_time)

                        if self.detect_face_time == 4:
                            # Initialize connection to the database
                            connection = pymysql.connect(
                                host="localhost", user="root", password="", db="pass_db"
                            )
                            try:
                                with connection.cursor() as cursor:
                                    self.existing_logs = self.check_existing_logs(
                                        cursor,
                                        self.get_student_id_from_filename(
                                            studentIds[matchIndex]
                                        ),
                                        now=datetime.now(),
                                    )

                            finally:
                                connection.close()
                        elif (
                            self.detect_face_time in [5, 6]
                            and self.existing_logs == False
                        ):
                            cv2.putText(
                                frame,
                                "Sending",
                                (x1 + 6, y2 + 50),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                0.60,
                                (255, 255, 255),
                                2,
                            )
                            now = datetime.now()
                            self.send_logs_to_db(
                                student_id=self.get_student_id_from_filename(
                                    studentIds[matchIndex]
                                ),
                                now=now,
                            )
                        elif self.logs_sent and self.detect_face_time in [7, 8]:
                            if self.existing_logs:
                                msg = "Logs already sent"
                            else:
                                msg = "Logs sent"
                            cv2.putText(
                                frame,
                                msg,
                                (x1 + 6, y2 + 50),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                0.60,
                                (255, 255, 255),
                                2,
                            )
                            print("Logs sent")
                        elif (
                            not self.logs_sent
                            and self.existing_logs
                            and self.detect_face_time >= 10
                        ):
                            cv2.putText(
                                frame,
                                "Logs already sent",
                                (x1 + 6, y2 + 50),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                0.60,
                                (255, 255, 255),
                                2,
                            )

                        if cur_face != studentIds[matchIndex]:
                            self.detect_face_time = 0
                            self.logs_sent = False

                        cur_face = studentIds[matchIndex]

                        if self.detect_face_time >= 15:
                            self.detect_face_time = 0

                    else:
                        self.detect_face_time = 0

                cv2.imshow("frame", frame)

                key = cv2.waitKey(1)
                if key == ord("q"):
                    break
            except Exception as e:
                if self.retries == self.count:
                    break
                self.count += 1
                print(f"Retry:{self.count}, {e}")
                pass

        cv2.destroyAllWindows()

    def send_logs_to_db(self, student_id, now):
        # Connect to the MySQL database
        connection = pymysql.connect(
            host="localhost", user="root", password="", db="pass_db"
        )

        try:
            with connection.cursor() as cursor:
                # Check if logs exist for the last (self.logout_minutes) minutes
                if self.check_existing_logs(cursor, student_id, datetime.now()):
                    print(
                        f"Logs already exist for the last {self.logout_minutes} minutes."
                    )
                else:
                    log_type = self.get_log_type_via_last_log_of_day(
                        cursor, student_id, datetime.now()
                    )
                    # Insert new log
                    query = "INSERT INTO tbl_logs (student_id, date_log, time_log, log_type) VALUES (%s, %s, %s, %s)"
                    cursor.execute(
                        query, (student_id, now.date(), now.time(), log_type)
                    )
                    connection.commit()
                    self.logs_sent = True
                    print("Log successfully inserted.")
        finally:
            connection.close()

    def check_existing_logs(self, cursor, student_id, now):
        # Function to check if logs exist for the last (self.logout_minutes) value minutes
        minutes_ago = now - timedelta(minutes=self.logout_minutes)

        query = "SELECT COUNT(*) FROM tbl_logs WHERE date_log = %s and time_log > %s and student_id = %s"
        cursor.execute(query, (minutes_ago.date(), minutes_ago.time(), student_id))
        count = cursor.fetchone()[0]

        return count > 0

    def get_log_type_via_last_log_of_day(self, cursor, student_id, now):
        query = "SELECT ID, LOG_TYPE FROM tbl_logs WHERE date_log = %s and student_id = %s order by ID desc"
        cursor.execute(query, (now.date(), student_id))
        last_log = cursor.fetchone()
        if last_log:
            return "LOGGED_OUT" if last_log[1] == "LOGGED_IN" else "LOGGED_IN"
        else:
            return "LOGGED_IN"

    def get_name_from_filename(self, filname):
        name = [s for s in filname if not s.isdigit()]

        return ("".join(name)).replace("-", " ")

    def get_student_id_from_filename(self, filename):
        student_id = [s for s in filename if s.isdigit()]
        return "".join(student_id)


# To run in terminal
# if __name__ == "__main__":
#     face_recognizer = FacialRecognitionWindow()
#     face_recognizer.face_recognition_func()
