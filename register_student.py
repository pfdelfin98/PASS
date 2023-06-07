import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow
import facial_recognition
import register_student
import student_management 
import admin_login
import dashboard
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import os

class RegisterStudentWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow 
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1186, 647)
        self.imageFilePath = None
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-1, 1, 261, 691))
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
        self.pushButton.setObjectName("pushButton")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(260, 0, 931, 61))
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
        self.label_10.setGeometry(QtCore.QRect(310, 80, 300, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color:black;")
        self.label_10.setObjectName("label_10")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(310, 160, 821, 391))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"box-shadow: 0px 0px 10px 2px rgba(0, 0, 0, 0.5);")
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
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(26, 26, 26);")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame_2)
        self.label_13.setGeometry(QtCore.QRect(380, 80, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(26, 26, 26);")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.frame_2)
        self.label_14.setGeometry(QtCore.QRect(40, 180, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(26, 26, 26);")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.frame_2)
        self.label_15.setGeometry(QtCore.QRect(380, 180, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(26, 26, 26);")
        self.label_15.setObjectName("label_15")
        self.firstNameText = QtWidgets.QPlainTextEdit(self.frame_2)
        self.firstNameText.setGeometry(QtCore.QRect(40, 130, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.firstNameText.setFont(font)
        self.firstNameText.setStyleSheet("border-radius:5px;\n"
"background-color: rgb(247, 247, 247);")
        self.firstNameText.setObjectName("firstNameText")
        self.middleNameText = QtWidgets.QPlainTextEdit(self.frame_2)
        self.middleNameText.setGeometry(QtCore.QRect(380, 130, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.middleNameText.setFont(font)
        self.middleNameText.setStyleSheet("border-radius:5px;\n"
"background-color: rgb(247, 247, 247);")
        self.middleNameText.setObjectName("middleNameText")


        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)

        self.imageLabel = QtWidgets.QLabel(self.frame_2)
        self.imageLabel.setGeometry(QtCore.QRect(40, 280, 211, 21))
        self.imageLabel.setObjectName("imageLabel")
        self.imageLabel.setText("Student Image")
        self.imageLabel.setFont(font)
        
        self.uploadImageBtn = QtWidgets.QPushButton(self.frame_2)
        self.uploadImageBtn.setGeometry(QtCore.QRect(40, 310, 211, 40))
        self.uploadImageBtn.setStyleSheet("background-color: rgb(255, 80, 80);"
                                        "color: rgb(255, 255, 255);"
                                        "border-radius: 5px;")
        self.uploadImageBtn.setObjectName("uploadImageBtn")
        self.uploadImageBtn.clicked.connect(self.uploadImage)

        self.imageStatusLabel = QtWidgets.QLabel(self.frame_2)
        self.imageStatusLabel.setGeometry(QtCore.QRect(40, 360, 211, 21))
        self.imageStatusLabel.setObjectName("imageStatusLabel")
        self.imageStatusLabel.setStyleSheet("color: rgb(26, 26, 26);")




        self.lastNameText = QtWidgets.QPlainTextEdit(self.frame_2)
        self.lastNameText.setGeometry(QtCore.QRect(40, 230, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lastNameText.setFont(font)
        self.lastNameText.setStyleSheet("border-radius:5px;\n"
"background-color: rgb(247, 247, 247);")
        self.lastNameText.setObjectName("lastNameText")
        self.comboBox = QtWidgets.QComboBox(self.frame_2)
        self.comboBox.setGeometry(QtCore.QRect(380, 230, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("border-radius:5px;\n"
"background-color: rgb(247, 247, 247);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.addStudentBtn = QtWidgets.QPushButton(self.frame_2)
        self.addStudentBtn.setGeometry(QtCore.QRect(570, 330, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setKerning(True)
        self.addStudentBtn.setFont(font)
        self.addStudentBtn.setAutoFillBackground(False)
        self.addStudentBtn.setStyleSheet("background-color: rgb(227, 30, 36);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
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
        self.pushButton.clicked.connect(self.open_dashboard)
        self.addStudentBtn.clicked.connect(self.addStudent)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_9.setText(_translate("MainWindow", "Admin Panel"))
        self.faceRecognitionBtn.setText(_translate("MainWindow", "Facial Recognition"))
        self.registerStudentBtn.setText(_translate("MainWindow", "Student Registration"))
        self.studentMgmtBtn.setText(_translate("MainWindow", "Student Management"))
        self.exitBtn.setText(_translate("MainWindow", "Exit"))
        self.exitBtn_2.setText(_translate("MainWindow", "Logout"))
        self.pushButton.setText(_translate("MainWindow", "Dashboard"))
        self.label.setText(_translate("MainWindow", "PASS: Personalized Authentication and Student Surveillance"))
        self.label_10.setText(_translate("MainWindow", "Student Registration"))
        self.label_11.setText(_translate("MainWindow", "New Student Form"))
        self.label_12.setText(_translate("MainWindow", "First Name"))
        self.label_13.setText(_translate("MainWindow", "Middle Name"))
        self.label_14.setText(_translate("MainWindow", "Last Name"))
        self.label_15.setText(_translate("MainWindow", "Course"))
        self.firstNameText.setPlaceholderText(_translate("MainWindow", "First Name"))
        self.middleNameText.setPlaceholderText(_translate("MainWindow", "Middle Name"))
        self.lastNameText.setPlaceholderText(_translate("MainWindow", "Last Name"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Bachelor of Science In Information Technology"))
        self.addStudentBtn.setText(_translate("MainWindow", "Submit"))
        self.uploadImageBtn.setText(_translate("MainWindow", "Click to Upload Student Image"))


    def uploadImage(self):
        # Open a file dialog to select an image file
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter("Images (*.png *.xpm *.jpg *.bmp *.gif)")
        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                image_path = selected_files[0]
                self.imageFilePath = image_path  # Assign the selected image path to imageFilePath
                # Do something with the selected image path
                print("Selected image:", image_path)
                self.imageStatusLabel.setText("Image inserted")

    def addStudent(self):
        first_name = self.firstNameText.toPlainText()
        middle_name = self.middleNameText.toPlainText()
        last_name = self.lastNameText.toPlainText()
        course = self.comboBox.currentText()
        image_path = self.imageFilePath  # Use the imageFilePath attribute

        db = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='pass_db'
        )
        cursor = db.cursor()

        # Insert student details
        query = "INSERT INTO tbl_student (first_name, middle_name, last_name, course) VALUES (%s, %s, %s, %s)"
        values = (first_name, middle_name, last_name, course)
        cursor.execute(query, values)
        db.commit()

        # Get the ID of the inserted student
        student_id = cursor.lastrowid

        # Insert the image filename
        if image_path:
            image_filename = f"{first_name}-{last_name}-{student_id}{os.path.splitext(image_path)[1]}"
            
            image_save_path = f"img/{image_filename}"  # Change 'img' to your desired folder path
            
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

        self.firstNameText.clear()
        self.middleNameText.clear()
        self.lastNameText.clear()

        # Clear the image file path
        self.imageFilePath = None


    def open_dashboard(self):
        print("Opening Dashboard...")
        self.MainWindow.close()
        self.dashboard_window = QMainWindow()
        self.ui = dashboard.Ui_Dashboard()
        self.ui.setupUi(self.dashboard_window)
        self.dashboard_window.show()
        
    def open_facial_recognition(self):
        # Add your code to open facial recognition here
        print("Opening Facial Recognition...")
        # self.MainWindow.close()
        self.facial_recognition_window = facial_recognition.FacialRecognitionWindow()
        self.facial_recognition_window.show()
        

    def open_register_student(self):
        # Add your code to open register student here
        print("Opening Register Student...")
        self.MainWindow.close()
        self.register_student_window = register_student.RegisterStudentWindow()
        self.register_student_window.show()

    def open_student_management(self):
        # Add your code to open student management here
        print("Opening Student Management...")
        self.MainWindow.close()
        self.student_management_window = student_management.StudentManagementWindow()
        self.student_management_window.show()

    def open_login_page(self):
        # Add your code to open the login page here
        print("Opening Login Page...")
        self.MainWindow.close()
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
