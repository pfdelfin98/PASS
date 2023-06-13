import sys
import os
import face_recognition
import register_student
import student_management
import admin_login
import cv2
import pickle
import numpy as np
import pymysql
from datetime import datetime, timedelta

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dashboard(object):
    def __init__(self) -> None:
        self.logs_sent = False
        self.existing = False

    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1186, 640)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-1, 1, 261, 2000))
        self.frame.setStyleSheet("background-color: rgb(227, 30, 36);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(80, 20, 101, 91))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("img/logo.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(44, 110, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.faceRecognitionBtn = QtWidgets.QPushButton(self.frame)
        self.faceRecognitionBtn.setGeometry(QtCore.QRect(40, 200, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.faceRecognitionBtn.setFont(font)
        self.faceRecognitionBtn.setStyleSheet(
            " background-color: transparent;\n" "color: white;\n" ""
        )
        self.faceRecognitionBtn.setStyleSheet(
            " background-color: transparent;\n"
            "color: white;\n"
            "text-align: left;\n"
            ""
        )
        self.faceRecognitionBtn.setObjectName("faceRecognitionBtn")
        self.registerStudentBtn = QtWidgets.QPushButton(self.frame)
        self.registerStudentBtn.setGeometry(QtCore.QRect(40, 250, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.registerStudentBtn.setFont(font)
        self.registerStudentBtn.setStyleSheet(
            " background-color: transparent;\n" "color: white;\n" ""
        )
        self.registerStudentBtn.setStyleSheet(
            " background-color: transparent;\n"
            "color: white;\n"
            "text-align: left;\n"
            ""
        )
        self.registerStudentBtn.setObjectName("registerStudentBtn")
        self.studentMgmtBtn = QtWidgets.QPushButton(self.frame)
        self.studentMgmtBtn.setGeometry(QtCore.QRect(40, 300, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.studentMgmtBtn.setFont(font)
        self.studentMgmtBtn.setStyleSheet(
            " background-color: transparent;\n" "color: white;\n" ""
        )
        self.studentMgmtBtn.setStyleSheet(
            " background-color: transparent;\n"
            "color: white;\n"
            "text-align: left;\n"
            ""
        )
        self.studentMgmtBtn.setObjectName("studentMgmtBtn")
        self.exitBtn = QtWidgets.QPushButton(self.frame)
        self.exitBtn.setGeometry(QtCore.QRect(40, 390, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.exitBtn.setFont(font)
        self.exitBtn.setStyleSheet(
            " background-color: transparent;\n" "color: white;\n" ""
        )
        self.exitBtn.setStyleSheet(
            " background-color: transparent;\n"
            "color: white;\n"
            "text-align: left;\n"
            ""
        )
        self.exitBtn.setObjectName("exitBtn")
        self.exitBtn_2 = QtWidgets.QPushButton(self.frame)
        self.exitBtn_2.setGeometry(QtCore.QRect(40, 340, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.exitBtn_2.setFont(font)
        self.exitBtn_2.setStyleSheet(
            " background-color: transparent;\n" "color: white;\n" ""
        )
        self.exitBtn_2.setStyleSheet(
            " background-color: transparent;\n"
            "color: white;\n"
            "text-align: left;\n"
            ""
        )
        self.exitBtn_2.setObjectName("exitBtn_2")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(261, -1, 2000, 61))
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(20, 10, 671, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(310, 90, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color:black;")
        self.label_10.setObjectName("label_10")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1186, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect button clicks to respective functions
        self.faceRecognitionBtn.clicked.connect(self.open_facial_recognition)
        self.registerStudentBtn.clicked.connect(self.open_register_student)
        self.studentMgmtBtn.clicked.connect(self.open_student_management)
        self.exitBtn.clicked.connect(QtWidgets.qApp.quit)
        self.exitBtn_2.clicked.connect(self.open_login_page)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_9.setText(_translate("MainWindow", "Admin Panel"))
        self.faceRecognitionBtn.setText(_translate("MainWindow", "Facial Recognition"))
        self.registerStudentBtn.setText(
            _translate("MainWindow", "Student Registration")
        )
        self.studentMgmtBtn.setText(_translate("MainWindow", "Student Management"))
        self.exitBtn.setText(_translate("MainWindow", "Exit"))
        self.exitBtn_2.setText(_translate("MainWindow", "Logout"))
        self.label.setText(
            _translate(
                "MainWindow",
                "PASS: Personalized Authentication and Student Surveillance",
            )
        )
        self.label_10.setText(_translate("MainWindow", "Dashboard"))

    def open_facial_recognition(self):
        # Add your code to open facial recognition here
        print("Opening Facial Recognition...")

        self.face_recognition_func()

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

        retries = 3
        count = 0
        cur_face = ""
        detect_face_time = 0
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
                    valid_face_accuracy_value = 0.5

                    if any(faceDis <= valid_face_accuracy_value):
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
                        detect_face_time += 1
                        print(self.logs_sent)
                        print(detect_face_time)
                        if detect_face_time == 4:
                            connection = pymysql.connect(
                                host="localhost", user="root", password="", db="pass_db"
                            )

                            try:
                                with connection.cursor() as cursor:
                                    self.existing = self.check_existing_logs(
                                        cursor,
                                        self.get_student_id_from_filename(
                                            studentIds[matchIndex]
                                        ),
                                    )

                            finally:
                                connection.close()
                        elif detect_face_time in [5, 6] and self.existing == False:
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
                        elif self.logs_sent and detect_face_time in [7, 8]:
                            if self.existing:
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
                            and self.existing
                            and detect_face_time >= 10
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
                            detect_face_time = 0
                            self.logs_sent = False

                        cur_face = studentIds[matchIndex]

                        if detect_face_time >= 15:
                            detect_face_time = 0

                    else:
                        detect_face_time = 0

                cv2.imshow("frame", frame)

                key = cv2.waitKey(1)
                if key == ord("q"):
                    break
            except Exception as e:
                if retries == count:
                    break
                count += 1
                print("Retry:", count)
                print(e)
                pass

        cv2.destroyAllWindows()

    def send_logs_to_db(self, student_id, now):
        # Connect to the MySQL database
        connection = pymysql.connect(
            host="localhost", user="root", password="", db="pass_db"
        )

        try:
            with connection.cursor() as cursor:
                # Check if logs exist for the last 5 minutes
                if self.check_existing_logs(cursor, student_id):
                    print("Logs already exist for the last 5 minutes.")
                else:
                    # Insert new log
                    query = "INSERT INTO tbl_logs (student_id, date_log, time_log) VALUES (%s, %s, %s)"
                    cursor.execute(query, (student_id, now.date(), now.time()))
                    connection.commit()
                    self.logs_sent = True
                    print("Log successfully inserted.")
        finally:
            connection.close()

    def check_existing_logs(self, cursor, student_id, minutes=5, now=datetime.now()):
        # Function to check if logs exist for the last 5 minutes
        five_minutes_ago = now - timedelta(minutes=minutes)
        print("-----")
        print(five_minutes_ago)
        print(student_id)
        print("-----")
        query = "SELECT COUNT(*) FROM tbl_logs WHERE date_log = %s and time_log > %s and student_id = %s"
        cursor.execute(
            query, (five_minutes_ago.date(), five_minutes_ago.time(), student_id)
        )
        count = cursor.fetchone()[0]
        print("-----")
        print(count)
        print("-----")
        return count > 0

    def get_name_from_filename(self, filname):
        name = [s for s in filname if not s.isdigit()]

        return ("".join(name)).replace("-", " ")

    def get_student_id_from_filename(self, filename):
        student_id = [s for s in filename if s.isdigit()]
        return "".join(student_id)

    def open_register_student(self):
        print("Opening Register Student...")
        self.MainWindow.hide()
        self.register_student_window = QtWidgets.QMainWindow()
        self.ui = register_student.RegisterStudentWindow()
        self.ui.setupUi(self.register_student_window)
        self.register_student_window.show()

    def open_student_management(self):
        print("Opening Student Management Page...")
        self.MainWindow.hide()
        self.student_management_window = QtWidgets.QMainWindow()
        self.ui = student_management.StudentManagementWindow()
        self.ui.setupUi(self.student_management_window)
        # Set the parent widget of the table widget
        self.ui.tableWidget.setParent(self.ui.centralwidget)
        # Load the students in the table
        self.ui.load_students()
        self.student_management_window.show()

    def open_login_page(self):
        print("Opening Login Page...")
        self.MainWindow.hide()
        self.admin_login_window = QtWidgets.QMainWindow()
        self.ui = admin_login.Ui_MainWindow()
        self.ui.setupUi(self.admin_login_window)
        self.admin_login_window.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Dashboard()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
