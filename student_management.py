import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QFileDialog, QDialog, QVBoxLayout, QLabel
import pymysql
import os
import cv2
import pickle
import numpy as np
import face_recognition
import openpyxl

import register_student
import student_management
import admin_login
import dashboard
from PyQt5.QtCore import QTimer

class StudentManagementWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow 
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1186, 647)
        self.imageFilePath = None
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # Add table widget
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(310, 150, 850, 450))
        self.tableWidget.setObjectName("tableWidget")

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
        self.faceRecognitionBtn.setGeometry(QtCore.QRect(3, 220, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.faceRecognitionBtn.setFont(font)
        self.faceRecognitionBtn.setStyleSheet(" background-color: transparent;\n"
"color: white;\n"
"")
        self.faceRecognitionBtn.setObjectName("faceRecognitionBtn")
        self.registerStudentBtn = QtWidgets.QPushButton(self.frame)
        self.registerStudentBtn.setGeometry(QtCore.QRect(17, 270, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.registerStudentBtn.setFont(font)
        self.registerStudentBtn.setStyleSheet(" background-color: transparent;\n"
"color: white;\n"
"")
        self.registerStudentBtn.setObjectName("registerStudentBtn")
        self.studentMgmtBtn = QtWidgets.QPushButton(self.frame)
        self.studentMgmtBtn.setGeometry(QtCore.QRect(0, 320, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.studentMgmtBtn.setFont(font)
        self.studentMgmtBtn.setStyleSheet(" background-color: transparent;\n"
"color: white;\n"
"")
        self.studentMgmtBtn.setObjectName("studentMgmtBtn")
        self.exitBtn = QtWidgets.QPushButton(self.frame)
        self.exitBtn.setGeometry(QtCore.QRect(-73, 410, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.exitBtn.setFont(font)
        self.exitBtn.setStyleSheet(" background-color: transparent;\n"
"color: white;\n"
"")
        self.exitBtn.setObjectName("exitBtn")
        self.exitBtn_2 = QtWidgets.QPushButton(self.frame)
        self.exitBtn_2.setGeometry(QtCore.QRect(-60, 360, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.exitBtn_2.setFont(font)
        self.exitBtn_2.setStyleSheet(" background-color: transparent;\n"
"color: white;\n"
"")
        self.exitBtn_2.setObjectName("exitBtn_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(1, 176, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(" background-color: transparent;\n"
"color: white;\n"
"")
   
        
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
        self.label_10.setGeometry(QtCore.QRect(310, 90, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
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

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

                # Connect button clicks to respective functions
        self.faceRecognitionBtn.clicked.connect(self.open_facial_recognition)
        self.registerStudentBtn.clicked.connect(self.open_register_student)
        self.studentMgmtBtn.clicked.connect(self.open_student_management)
        self.exitBtn.clicked.connect(QtWidgets.qApp.quit)
        self.exitBtn_2.clicked.connect(self.open_login_page)
        self.pushButton.clicked.connect(self.open_dashboard)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Student Management"))
        self.label_9.setText(_translate("MainWindow", "Admin Panel"))
        self.pushButton.setText(_translate("MainWindow", "Dashboard"))
        self.faceRecognitionBtn.setText(_translate("MainWindow", "Facial Recognition"))
        self.registerStudentBtn.setText(_translate("MainWindow", "Student Registration"))
        self.studentMgmtBtn.setText(_translate("MainWindow", "Student Management"))
        self.exitBtn.setText(_translate("MainWindow", "Exit"))
        self.exitBtn_2.setText(_translate("MainWindow", "Logout"))
        self.label.setText(_translate("MainWindow", "PASS: Personalized Authentication and Student Surveillance"))
        self.label_10.setText(_translate("MainWindow", "Student Management"))
    
    def load_students(self):
        connection = pymysql.connect(host='localhost', user='root', password='', db='pass_db')
        self.connection = connection  # Store the connection reference to access it later
        cursor = connection.cursor()

        # Fetch student data from the database
        query = "SELECT id, first_name, middle_name, last_name, course FROM tbl_student"
        cursor.execute(query)
        students = cursor.fetchall()

        # Display students in the table
        row_count = len(students)
        column_count = 7  # Increase column count for edit and delete buttons

        self.tableWidget.setRowCount(row_count)
        self.tableWidget.setColumnCount(column_count)

        header_labels = ["First Name", "Middle Name", "Last Name", "Course", "View Logs", "Edit", "Delete"]
        self.tableWidget.setHorizontalHeaderLabels(header_labels)

        for i, student in enumerate(students):
            student_id = student[0]  # Get the student ID
            for j in range(column_count - 3):  # Adjust the range
                item = QTableWidgetItem(str(student[j + 1]))  # Update the index of the student details
                self.tableWidget.setItem(i, j, item)  # Update the column index

            # Create and set the edit button
            edit_button = QPushButton("Edit")
            edit_button.clicked.connect(lambda checked, student_id=student_id: self.edit_student(student_id))
            self.tableWidget.setCellWidget(i, column_count - 2, edit_button)

            # Create and set the delete button
            delete_button = QPushButton("Delete")
            delete_button.clicked.connect(lambda checked, student_id=student_id: self.delete_student(student_id))
            self.tableWidget.setCellWidget(i, column_count - 1, delete_button)


            # Create and set the delete button
            view_logs_button = QPushButton("View Logs")
            view_logs_button.clicked.connect(lambda checked, student_id=student_id: self.view_logs(student_id))
            self.tableWidget.setCellWidget(i, column_count - 3, view_logs_button)

        cursor.close()

        # Schedule the next update after 1 second
        QTimer.singleShot(1000, self.load_students)

    def start_loading_students(self):
        # Start loading the students initially
        self.load_students()


    def view_logs(self, student_id):
        print("Edit Student ID:", student_id)


    def edit_student(self, student_id):
        print("Edit Student ID:", student_id)


    def delete_student(self, student_id):
        print("Delete Student ID:", student_id)

    def open_dashboard(self):
        print("Opening Dashboard...")
        self.MainWindow.hide()
        self.dashboard_window = QMainWindow()
        self.ui = dashboard.Ui_Dashboard()
        self.ui.setupUi(self.dashboard_window)
        self.dashboard_window.show()

    def open_facial_recognition(self):
        # Add your code to open facial recognition here
        print("Opening Facial Recognition...")
        # self.MainWindow.close()
        #self.facial_recognition_window = QtWidgets.QMainWindow()
        #self.ui = facial_recognition.FacialRecognitionWindow()
        #self.ui.setupUi(self.facial_recognition_window)
        #self.facial_recognition_window.show()
        # video = cv2.VideoCapture(0)

        # while True:
        #     suc, img = video.read()

        #     cv2.imshow("frame", img)

        #     if cv2.waitKey(1) & 0xFF == ord('q'):
        #         break

        # video.release()
        # cv2.destroyAllWindows()
        self.face_recognition_func()

    def face_recognition_func(self):
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        # Importing student images
        folderModePath = 'images'
        pathList = os.listdir(folderModePath)
        imgList = []
        studentIds = []
        for path in pathList:
            imgList.append(cv2.imread(os.path.join(folderModePath, path)))

        # Load the encoding file
        print("Loading Encoding File ....")
        file = open('FaceEncodeFile.p', 'rb')
        encodeListKnownWithIds = pickle.load(file)
        file.close()
        encodeListKnown, studentIds = encodeListKnownWithIds
        print("Encoding File Loaded")

        retries = 3
        count = 0

        while True:
            try:
                ret, frame = cap.read()

                imgS = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
                imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

                faceCurFrame = face_recognition.face_locations(imgS)
                encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)


                for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
                    matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
                    faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

                    matchIndex = np.argmin(faceDis)


                    if matches[matchIndex]:
                        name = studentIds[matchIndex].upper()
                        y1, x2, y2, x1 = faceLoc
                        y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                        cv2.rectangle(frame, (x1, y2-35), (x2, y2), (0, 255, 0), cv2.FILLED)
                        cv2.putText(frame, name, (x1+6, y2-6), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

                cv2.imshow('frame', frame)

                key = cv2.waitKey(1)
                if key == ord('q'):
                    break
            except Exception as e:
                if retries == count:
                    break
                count+=1
                print("Retry:", count)
                print(e)
                pass

        cv2.destroyAllWindows()


    def open_register_student(self):
        # Add your code to open register student here
        print("Opening Register Student...")
        self.MainWindow.hide()
        self.register_student_window = QtWidgets.QMainWindow()
        self.ui = register_student.RegisterStudentWindow()
        self.ui.setupUi(self.register_student_window)
        self.register_student_window.show()

    def open_student_management(self):
        # Add your code to open student management here
        print("Opening Student Management Page...")
        self.MainWindow.hide()  # Hide the main window instead of closing it
        # Create the student management window
        self.student_management_window = QtWidgets.QMainWindow()
        self.ui = student_management.StudentManagementWindow()
        self.ui.setupUi(self.student_management_window)
        # Set the parent widget of the table widget
        self.ui.tableWidget.setParent(self.ui.centralwidget)
        # Load the students in the table
        self.ui.load_students()
        self.student_management_window.show()

    def open_login_page(self):
        # Add your code to open the login page here
        print("Opening Login Page...")
        self.MainWindow.hide()
        self.admin_login_window = QtWidgets.QMainWindow()
        self.ui = admin_login.Ui_MainWindow()
        self.ui.setupUi(self.admin_login_window)
        self.admin_login_window.show()



    # ...
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = StudentManagementWindow()
    ui.setupUi(MainWindow)
    ui.load_students()
    MainWindow.show()
    sys.exit(app.exec_())
