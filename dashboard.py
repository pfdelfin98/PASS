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
from PyQt5.QtWidgets import (
    QMainWindow,
    QTableWidget,
    QTableWidgetItem,
    QPushButton,
    QFileDialog,
    QDialog,
    QVBoxLayout,
    QLabel,
)
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from about_dialog import AboutDialog
from PyQt5.QtCore import QTimer
from datetime import datetime, timedelta
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableWidget,
    QVBoxLayout,
    QScrollArea,
    QWidget,
)


class Ui_Dashboard(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setWindowFlags(
            MainWindow.windowFlags()
            & ~QtCore.Qt.WindowMinimizeButtonHint
            & ~QtCore.Qt.WindowMaximizeButtonHint
        )

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1186, 640)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # Add table widget
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(310, 150, 850, 450))
        self.tableWidget.setObjectName("tableWidget")
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
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
        self.exitBtn.setGeometry(QtCore.QRect(40, 350, 221, 31))
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
        self.exitBtn_2.setGeometry(QtCore.QRect(40, 400, 221, 31))
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

        self.aboutBtn = QtWidgets.QPushButton(self.frame)
        self.aboutBtn.setGeometry(QtCore.QRect(40, 450, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.aboutBtn.setFont(font)
        self.aboutBtn.setStyleSheet(
            " background-color: transparent;\n" "color: white;\n" ""
        )
        self.aboutBtn.setStyleSheet(
            " background-color: transparent;\n"
            "color: white;\n"
            "text-align: left;\n"
            ""
        )
        self.aboutBtn.setObjectName("aboutBtn")

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
        self.aboutBtn.clicked.connect(self.open_about)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_9.setText(_translate("MainWindow", "Admin Panel"))
        self.faceRecognitionBtn.setText(_translate("MainWindow", "Facial Recognition"))
        self.registerStudentBtn.setText(
            _translate("MainWindow", "Student Registration")
        )
        self.studentMgmtBtn.setText(_translate("MainWindow", "Student Management"))
        self.aboutBtn.setText(_translate("MainWindow", "About System"))
        self.exitBtn.setText(_translate("MainWindow", "Exit"))
        self.exitBtn_2.setText(_translate("MainWindow", "Logout"))
        self.label.setText(
            _translate(
                "MainWindow",
                "PASS: Personalized Authentication and Student Surveillance",
            )
        )
        self.label_10.setText(_translate("MainWindow", "Dashboard"))

    def load_logs(self):
        connection = pymysql.connect(
            host="localhost", user="root", password="", db="pass_db"
        )
        cursor = connection.cursor()

        delete_query = "DELETE FROM tbl_logs WHERE date_log < %s"
        week_ago = datetime.now() - timedelta(days=7)
        cursor.execute(delete_query, (week_ago.date(),))
        connection.commit()

        query = "SELECT  tbl_student.image, tbl_student.first_name, tbl_student.last_name, tbl_logs.date_log, tbl_logs.time_log FROM tbl_logs LEFT JOIN tbl_student ON tbl_logs.student_id = tbl_student.id"
        cursor.execute(query)
        logs = cursor.fetchall()

        row_count = len(logs)
        column_count = 5  # Increase the column count for the image column

        self.tableWidget.setRowCount(row_count)
        self.tableWidget.setColumnCount(column_count)

        header_labels = ["Image", "First Name", "Last Name", "Date Log", "Time Log"]
        self.tableWidget.setHorizontalHeaderLabels(header_labels)

        for row, log in enumerate(logs):
            image_filename, first_name, last_name, date_log, time_log = log

            # Create a QLabel and set the image pixmap
            image_label = QLabel()
            image_path = os.path.join("images", str(image_filename))
            pixmap = QPixmap(image_path)
            if not pixmap.isNull():
                pixmap = pixmap.scaledToWidth(100)  # Adjust the width as needed
                pixmap = pixmap.scaledToHeight(100)  # Adjust the height as needed
                image_label.setPixmap(pixmap)
                image_label.setAlignment(
                    Qt.AlignCenter
                )  # Center the image in the label

            self.tableWidget.setCellWidget(row, 0, image_label)

            self.tableWidget.setItem(row, 1, QTableWidgetItem(first_name))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(last_name))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(str(date_log)))
            self.tableWidget.setItem(row, 4, QTableWidgetItem(str(time_log)))

        cursor.close()

        # Schedule the next update after 1 second
        QTimer.singleShot(1000, self.load_logs)

    def start_loading_students(self):
        # Start loading the students initially
        self.load_logs()

    def open_facial_recognition(self):
        from facial_recognition import FacialRecognitionWindow

        face_recognition = FacialRecognitionWindow()
        # Add your code to open facial recognition here
        print("Opening Facial Recognition...")

        face_recognition.face_recognition_func()

    def open_about(self):
        print("Opening About System Dialog")
        dialog = AboutDialog()
        dialog.setupUi()
        dialog.show()

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
    ui.load_logs()
    MainWindow.show()
    sys.exit(app.exec_())
