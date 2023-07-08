import sys
import os
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow
from encodegenerator import encodegenerator
import student_management
import admin_login
import dashboard
import logs
import pymysql
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from about_dialog import AboutDialog
from success_dialog import SuccessDialog
from error_dialog2 import ErrorDialog
from error_image import ErrorImageDialog

from datetime import datetime, timedelta

import auto_export_reset as auto


class RegisterStudentWindow(object):
    def __init__(self):
        # Export and Delete Analytics Every Monday (Check Every Second)
        self.day_of_export = auto.AutomaticExportResetLogs().day_of_export
        self.timer_second = 2
        self.timer = QTimer()
        self.timer.timeout.connect(self.analytics_reset_export_check)
        self.timer.start(self.timer_second * 1000)  # Execute every set self.time_second

    def analytics_reset_export_check(self):
        print(self.day_of_export)
        auto_export = auto.AutomaticExportResetLogs()

        current_date = datetime.now().date()
        prev_sunday = current_date - timedelta(days=1)
        prev_monday = current_date - timedelta(days=7)
        current_weekday = current_date.weekday()

        if auto.DAYS_IN_WEEK[current_weekday] == self.day_of_export:
            if auto_export.check_if_logs_found(
                prev_sunday=prev_sunday, prev_monday=prev_monday
            ):
                print("Exporting...")
                auto_export.export_logs(
                    prev_sunday=prev_sunday, prev_monday=prev_monday
                )
                auto_export.export_delete_analytics(
                    prev_sunday=prev_sunday, prev_monday=prev_monday
                )
                print("Exporting Done!")
            else:
                self.timer.stop()
                return
        else:
            print(f"Today is not {self.day_of_export}")
            self.timer.stop()
            return

    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setWindowFlags(
            MainWindow.windowFlags()
            & ~QtCore.Qt.WindowMinimizeButtonHint
            & ~QtCore.Qt.WindowMaximizeButtonHint
        )
        MainWindow.setObjectName("MainWindow")
        # MainWindow.resize(1200, 700)
        self.MainWindow.showMaximized()
        MainWindow.setWindowFlags(
            MainWindow.windowFlags()
            & ~QtCore.Qt.WindowCloseButtonHint  # Remove the close button
        )
        self.imageFilePath = None
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
        self.label_4.setPixmap(QtGui.QPixmap("img/logo2.png"))
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
        self.faceRecognitionBtn.setGeometry(QtCore.QRect(40, 300, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.faceRecognitionBtn.setFont(font)
        self.faceRecognitionBtn.setStyleSheet(
            " background-color: transparent;\n"
            "color: white;\n"
            "text-align: left;\n"
            ""
        )
        self.faceRecognitionBtn.setObjectName("faceRecognitionBtn")
        self.registerStudentBtn = QtWidgets.QPushButton(self.frame)
        self.registerStudentBtn.setGeometry(QtCore.QRect(40, 350, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.registerStudentBtn.setFont(font)
        self.registerStudentBtn.setStyleSheet(
            " background-color: transparent;\n"
            "color: white;\n"
            "text-align: left;\n"
            ""
        )
        self.registerStudentBtn.setObjectName("registerStudentBtn")
        self.studentMgmtBtn = QtWidgets.QPushButton(self.frame)
        self.studentMgmtBtn.setGeometry(QtCore.QRect(40, 400, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.studentMgmtBtn.setFont(font)
        self.studentMgmtBtn.setStyleSheet(
            " background-color: transparent;\n"
            "color: white;\n"
            "text-align: left;\n"
            ""
        )
        self.studentMgmtBtn.setObjectName("studentMgmtBtn")
        self.exitBtn = QtWidgets.QPushButton(self.frame)
        self.exitBtn.setGeometry(QtCore.QRect(40, 450, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.exitBtn.setFont(font)
        self.exitBtn.setStyleSheet(
            " background-color: transparent;\n"
            "color: white;\n"
            "text-align: left;\n"
            ""
        )
        self.exitBtn.setObjectName("exitBtn")
        self.exitBtn_2 = QtWidgets.QPushButton(self.frame)
        self.exitBtn_2.setGeometry(QtCore.QRect(40, 500, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.exitBtn_2.setFont(font)
        self.exitBtn_2.setStyleSheet(
            " background-color: transparent;\n"
            "color: white;\n"
            "text-align: left;\n"
            ""
        )
        self.exitBtn_2.setObjectName("exitBtn_2")

        self.aboutBtn = QtWidgets.QPushButton(self.frame)
        self.aboutBtn.setGeometry(QtCore.QRect(40, 550, 221, 31))
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

        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(40, 200, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(
            " background-color: transparent;\n"
            "color: white;\n"
            "text-align: left;\n"
            ""
        )

        self.pushButton.setObjectName("pushButton")

        self.pushButton2 = QtWidgets.QPushButton(self.frame)
        self.pushButton2.setGeometry(QtCore.QRect(40, 250, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton2.setFont(font)
        self.pushButton2.setStyleSheet(
            " background-color: transparent;\n"
            "color: white;\n"
            "text-align: left;\n"
            ""
        )

        self.pushButton2.setObjectName("pushButton2")

        # self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        # self.frame_3.setGeometry(QtCore.QRect(261, -1, 2000, 70))
        # self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        # self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.frame_3.setObjectName("frame_3")
        # self.label = QtWidgets.QLabel(self.frame_3)
        # self.label.setGeometry(QtCore.QRect(20, 10, 671, 41))
        # font = QtGui.QFont()
        # font.setFamily("Arial")
        # font.setPointSize(12)
        # self.label.setFont(font)
        # self.label.setObjectName("label")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(310, 80, 300, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color:black;")
        self.label_10.setObjectName("label_10")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(310, 160, 1240, 500))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);\n")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setGeometry(QtCore.QRect(40, 20, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color:black;")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame_2)
        self.label_12.setGeometry(QtCore.QRect(40, 80, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(26, 26, 26);")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame_2)
        self.label_13.setGeometry(QtCore.QRect(380, 80, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(26, 26, 26);")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.frame_2)
        self.label_14.setGeometry(QtCore.QRect(740, 80, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(26, 26, 26);")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.frame_2)
        self.label_15.setGeometry(QtCore.QRect(380, 180, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(26, 26, 26);")
        self.label_15.setObjectName("label_15")
        self.firstNameText = QtWidgets.QPlainTextEdit(self.frame_2)
        self.firstNameText.setGeometry(QtCore.QRect(40, 130, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.firstNameText.setFont(font)
        self.firstNameText.setStyleSheet(
            "border-radius:5px;\n" "background-color: rgb(247, 247, 247);"
        )
        self.firstNameText.setObjectName("firstNameText")
        self.firstNameText.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.middleNameText = QtWidgets.QPlainTextEdit(self.frame_2)
        self.middleNameText.setGeometry(QtCore.QRect(380, 130, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.middleNameText.setFont(font)
        self.middleNameText.setStyleSheet(
            "border-radius:5px;\n" "background-color: rgb(247, 247, 247);"
        )
        self.middleNameText.setObjectName("middleNameText")
        self.middleNameText.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)

        self.imageLabel = QtWidgets.QLabel(self.frame_2)
        self.imageLabel.setGeometry(QtCore.QRect(740, 190, 211, 21))
        self.imageLabel.setObjectName("imageLabel")
        self.imageLabel.setText("Sex")
        self.imageLabel.setFont(font)

        self.comboBox1 = QtWidgets.QComboBox(self.frame_2)
        self.comboBox1.setGeometry(QtCore.QRect(740, 230, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.comboBox1.setFont(font)
        self.comboBox1.setStyleSheet(
            "border-radius:5px;\n" "background-color: rgb(247, 247, 247);"
        )
        self.comboBox1.addItem("Male")
        self.comboBox1.addItem("Female")

        self.imageLabel = QtWidgets.QLabel(self.frame_2)
        self.imageLabel.setGeometry(QtCore.QRect(40, 290, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.imageLabel.setFont(font)
        self.imageLabel.setStyleSheet("color: rgb(26, 26, 26);")
        self.imageLabel.setObjectName("imageLabel")
        self.imageLabel.setText("Student Image")

        self.uploadImageBtn = QtWidgets.QPushButton(self.frame_2)
        self.uploadImageBtn.setGeometry(QtCore.QRect(40, 330, 211, 40))
        self.uploadImageBtn.setStyleSheet(
            """
                QPushButton {
                    background-color: #dc3545;  
                    border: none;
                    color: white;
                    padding: 8px 16px;
                    border-radius: 4px;
                    font-family: Arial;
                    font-size: 8pt;
                }

                QPushButton:hover {
                    background-color: #c82333;  /* Darker shade on hover */
                }
                """
        )
        self.uploadImageBtn.setObjectName("uploadImageBtn")
        self.uploadImageBtn.clicked.connect(self.uploadImage)

        self.imageStatusLabel = QtWidgets.QLabel(self.frame_2)
        self.imageStatusLabel.setGeometry(QtCore.QRect(40, 370, 211, 21))
        self.imageStatusLabel.setObjectName("imageStatusLabel")
        self.imageStatusLabel.setStyleSheet("color: rgb(26, 26, 26);")

        self.lastNameText = QtWidgets.QPlainTextEdit(self.frame_2)
        self.lastNameText.setGeometry(QtCore.QRect(740, 130, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.lastNameText.setFont(font)
        self.lastNameText.setStyleSheet(
            "border-radius:5px;\n" "background-color: rgb(247, 247, 247);"
        )
        self.lastNameText.setObjectName("lastNameText")
        self.lastNameText.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.srCodeLabel = QtWidgets.QLabel(self.frame_2)
        self.srCodeLabel.setGeometry(QtCore.QRect(40, 190, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.srCodeLabel.setFont(font)
        self.srCodeLabel.setStyleSheet("color: rgb(26, 26, 26);")
        self.srCodeLabel.setObjectName("srCodeLabel")
        self.srCodeLabel.setText("SR Code")
        self.srcodetext = QtWidgets.QLineEdit(self.frame_2)
        self.srcodetext.setGeometry(QtCore.QRect(40, 230, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.srcodetext.setFont(font)
        self.srcodetext.setStyleSheet(
            "border-radius:5px;\n" "background-color: rgb(247, 247, 247);"
        )
        self.srcodetext.setObjectName("srcodetext")

        regex = QtCore.QRegExp(r"^[0-9-]*$")
        validator = QtGui.QRegExpValidator(regex, self.srcodetext)
        self.srcodetext.setValidator(validator)

        self.comboBox = QtWidgets.QComboBox(self.frame_2)
        self.comboBox.setGeometry(QtCore.QRect(380, 230, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet(
            "border-radius:5px;\n" "background-color: rgb(247, 247, 247);"
        )
        self.comboBox.addItem("BS In Information Technology")
        self.comboBox.addItem("BS in Elementary Education")
        self.comboBox.addItem("BS in Secondary Education")
        self.comboBox.addItem("BS in Accountancy")
        self.comboBox.addItem("BS in Management Accounting")
        self.comboBox.addItem("BS in Business Administration")
        self.comboBox.addItem("BS in Computer Engineering")
        self.comboBox.addItem("BS in Computer Science")
        self.comboBox.addItem("Bs in Industrial Technology")
        self.comboBox.addItem("BS in Food Technology")
        self.comboBox.addItem("BS in Nursing")
        self.comboBox.addItem("BS in Nutrition and Dietetics")
        self.comboBox.addItem("BS in Criminology")
        self.comboBox.addItem("BS in Psychology")
        self.comboBox.addItem("BS in Hospitality Management")
        self.comboBox.addItem("BS in Tourism Management")
        self.comboBox.addItem("BS in Computer Engineering")
        self.comboBox.addItem("BS in Fisheries and Aquatic Sciences")
        self.comboBox.addItem("BA in Communication")
        self.comboBox.addItem("BS in Fisheries and Aquatic Sciences")
        self.comboBox.addItem("BS in Physical Education")
        self.comboBox.addItem("BS in Teacher Education")

        # search bar
        self.searchLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.searchLineEdit.setGeometry(QtCore.QRect(1200, 95, 200, 30))
        self.searchLineEdit.setObjectName("searchLineEdit")

        self.searchLabel = QtWidgets.QLabel(self.centralwidget)
        self.searchLabel.setGeometry(QtCore.QRect(1130, 95, 70, 30))
        self.searchLabel.setObjectName("searchLabel")
        self.searchLabel.setText("Import Data:")

        self.exportDataBtn = QtWidgets.QPushButton(self.centralwidget)
        self.exportDataBtn.setGeometry(QtCore.QRect(1420, 94, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.exportDataBtn.setFont(font)
        self.exportDataBtn.setObjectName("exportDataBtn")
        self.exportDataBtn.setText("Enter")
        self.exportDataBtn.setStyleSheet(
            """
            QPushButton {
                background-color: #dc3545;  
                border: none;
                color: white;
                padding: 8px 16px;
                border-radius: 4px;
                font-family: Arial;
                font-size: 10pt;
            }

            QPushButton:hover {
                background-color: #c82333;  
            }
            """
        )

        self.addStudentBtn = QtWidgets.QPushButton(self.frame_2)
        self.addStudentBtn.setGeometry(QtCore.QRect(1000, 440, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setKerning(True)
        self.addStudentBtn.setFont(font)
        self.addStudentBtn.setAutoFillBackground(False)
        self.addStudentBtn.setStyleSheet(
            """
                QPushButton {
                    background-color: #dc3545;  
                    border: none;
                    color: white;
                    padding: 10px 16px;
                    border-radius: 4px;
                    font-family: Arial;
                    font-size: 8pt;
                }

                QPushButton:hover {
                    background-color: #c82333;  /* Darker shade on hover */
                }
                """
        )
        self.addStudentBtn.setAutoDefault(False)
        self.addStudentBtn.setDefault(False)
        self.addStudentBtn.setFlat(False)
        self.addStudentBtn.setObjectName("addStudentBtn")
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

        self.faceRecognitionBtn.clicked.connect(self.open_facial_recognition)
        self.registerStudentBtn.clicked.connect(self.open_register_student)
        self.studentMgmtBtn.clicked.connect(self.open_student_management)
        self.exitBtn.clicked.connect(QtWidgets.qApp.quit)
        self.exitBtn_2.clicked.connect(self.open_login_page)
        self.aboutBtn.clicked.connect(self.open_about)
        self.pushButton.clicked.connect(self.open_dashboard)
        self.pushButton2.clicked.connect(self.open_logs)
        self.addStudentBtn.clicked.connect(self.addStudent)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(
            _translate(
                "MainWindow",
                "PASS: Personalized Authentication and Student Surveillance",
            )
        )
        self.label_9.setText(_translate("MainWindow", "      PASS"))
        self.faceRecognitionBtn.setText(_translate("MainWindow", "Facial Recognition"))
        self.registerStudentBtn.setText(
            _translate("MainWindow", "Student Registration")
        )
        self.studentMgmtBtn.setText(_translate("MainWindow", "Student Management"))
        self.exitBtn.setText(_translate("MainWindow", "Exit"))
        self.exitBtn_2.setText(_translate("MainWindow", "Logout"))
        self.aboutBtn.setText(_translate("MainWindow", "About System"))
        self.pushButton.setText(_translate("MainWindow", "Dashboard"))
        self.pushButton2.setText(_translate("MainWindow", "Logs"))

        # self.label.setText(
        #     _translate(
        #         "MainWindow",
        #         "PASS: Personalized Authentication and Student Surveillance",
        #     )
        # )
        self.label_10.setText(_translate("MainWindow", "Student Registration"))
        self.label_11.setText(_translate("MainWindow", "New Student Form"))
        self.label_12.setText(_translate("MainWindow", "First Name"))
        self.label_13.setText(_translate("MainWindow", "Middle Name"))
        self.label_14.setText(_translate("MainWindow", "Last Name"))
        self.label_15.setText(_translate("MainWindow", "Course"))
        self.firstNameText.setPlaceholderText(_translate("MainWindow", "First Name"))
        self.middleNameText.setPlaceholderText(_translate("MainWindow", "Middle Name"))
        self.lastNameText.setPlaceholderText(_translate("MainWindow", "Last Name"))
        self.srcodetext.setPlaceholderText(_translate("MainWindow", "SR Code"))

        self.addStudentBtn.setText(_translate("MainWindow", "Submit"))
        self.uploadImageBtn.setText(
            _translate("MainWindow", "Click to Upload Student Image")
        )

    def uploadImage(self):
        # Open a file dialog to select an image file
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter("Images (*.png *.xpm *.jpg *.bmp *.gif)")
        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                image_path = selected_files[0]
                if image_path.lower().endswith(".jpg"):
                    self.imageFilePath = (
                        image_path  # Assign the selected image path to imageFilePath
                    )
                    # Do something with the selected image path
                    print("Selected image:", image_path)
                    self.imageStatusLabel.setText("Image inserted")
                else:
                    dialog = ErrorImageDialog()
                    dialog.setupUi()
                    dialog.exec_()
                    return

    def addStudent(self):
        first_name = self.firstNameText.toPlainText()
        middle_name = self.middleNameText.toPlainText()
        last_name = self.lastNameText.toPlainText()
        course = self.comboBox.currentText()
        srcode = self.srcodetext.text()
        age = self.comboBox1.currentText()
        image_path = self.imageFilePath

        if not (first_name and middle_name and last_name and srcode and image_path):
            print("Please provide all the required student details.")
            dialog = ErrorDialog()
            dialog.setupUi()
            dialog.exec_()
            return

        department = self.get_department(course)

        db = pymysql.connect(host="localhost", user="root", password="", db="pass_db")
        cursor = db.cursor()

        query = "INSERT INTO tbl_student (first_name, middle_name, last_name, course, department, sr_code, gender) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (first_name, middle_name, last_name, course, department, srcode, age)
        cursor.execute(query, values)
        db.commit()

        student_id = cursor.lastrowid

        if image_path:
            image_filename = f"{first_name}-{last_name}-{student_id}{os.path.splitext(image_path)[1]}"

            image_save_path = (
                f"images/{image_filename}"  # Change 'img' to your desired folder path
            )

            # Save the image to the local drive
            os.rename(image_path, image_save_path)

            # Update the student record with the image filename
            update_query = "UPDATE tbl_student SET image = %s WHERE id = %s"
            update_values = (image_filename, student_id)
            cursor.execute(update_query, update_values)
            db.commit()

        cursor.close()
        db.close()

        print("Student inserted successfully!")
        dialog = SuccessDialog()
        dialog.setupUi()
        dialog.exec_()

        self.firstNameText.clear()
        self.middleNameText.clear()
        self.lastNameText.clear()
        self.srcodetext.clear()
        # Clear the image file path
        self.imageFilePath = None
        encodegenerator()

    def get_department(self, course):
        departments = {
            "CABEIHM": [
                "BS in Accountancy",
                "BS in Management Accounting",
                "BS in Business Administration",
                "BS in Hospitality Management",
                "BS in Tourism Management",
            ],
            "CAS": [
                "BA in Communication",
                "BS in Criminology",
                "BS in Food Technology",
                "BS in Psychology",
                "BS in Fisheries and Aquatic Sciences",
            ],
            "CICS": ["BS in Computer Science", "BS in Information Technology"],
            "CET": ["BS in Computer Engineering", "BS in Industrial Technology"],
            "CONAHS": ["BS in Nursing", "BS in Nutrition and Dietetics"],
            "CTE": [
                "BS in Elementary Education",
                "BS in Secondary Education",
                "BS in Physical Education",
                "Professional Teacher Education",
            ],
        }
        departments_casefold = {}

        for key, value in departments.items():
            departments_casefold[key] = [course.casefold() for course in value]

        department = None
        for dept, courses in departments_casefold.items():
            if course.casefold() in courses:
                department = dept
                break

        return department

    def open_dashboard(self):
        print("Opening Dashboard...")
        self.MainWindow.hide()
        self.dashboard_window = QtWidgets.QMainWindow()
        self.ui = dashboard.Ui_Dashboard()
        self.ui.setupUi(self.dashboard_window)
        # self.ui.tableWidget.setParent(self.ui.centralwidget)
        # self.ui.load_logs()
        self.dashboard_window.show()

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
        # Add your code to open register student here
        print("Opening Register Student...")
        # self.MainWindow.hide()
        # self.register_student_window = register_student.RegisterStudentWindow()
        # self.register_student_window.show()

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

    def open_logs(self):
        print("Opening Logs...")
        self.MainWindow.hide()
        self.logs_window = QtWidgets.QMainWindow()
        self.ui = logs.Logs()
        self.ui.setupUi(self.logs_window)
        self.ui.tableWidget.setParent(self.ui.centralwidget)
        self.ui.load_logs()
        self.logs_window.show()

    def open_login_page(self):
        # Add your code to open the login page here
        print("Opening Login Page...")
        self.MainWindow.hide()
        self.admin_login_window = QtWidgets.QMainWindow()
        self.ui = admin_login.Ui_MainWindow()
        self.ui.setupUi(self.admin_login_window)
        self.admin_login_window.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = RegisterStudentWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
