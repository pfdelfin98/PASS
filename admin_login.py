import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
import dashboard
from error_login import ErrorDialog

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow 
        MainWindow.setWindowFlags(MainWindow.windowFlags() & ~QtCore.Qt.WindowMinimizeButtonHint & ~QtCore.Qt.WindowMaximizeButtonHint)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(917, 600)
        MainWindow.setStyleSheet("background-color: rgb(247, 247, 247);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 421, 2000))
        self.frame.setStyleSheet("background-color: rgb(227, 30, 36);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(90, 210, 271, 111))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(23, 310, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n" "text-align: center;\n")
      
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(53, 340, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);\n" "text-align: center;\n")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(73, 370, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);\n" "text-align: center;\n")
        self.label_8.setObjectName("label_8")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(130, 60, 170, 160))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("img/logo.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(470, 70, 391, 411))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.usernameText = QtWidgets.QPlainTextEdit(self.frame_2)
        self.usernameText.setGeometry(QtCore.QRect(40, 140, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.usernameText.setFont(font)
        self.usernameText.setStyleSheet("border-radius:5px;\n"
"background-color: rgb(247, 247, 247);")
        self.usernameText.setObjectName("usernameText")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(40, 110, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(65, 65, 65);")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(160, 20, 101, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(65, 65, 65);")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(40, 220, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border-radius:5px;\n"
"background-color: rgb(247, 247, 247);")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.loginButton = QtWidgets.QPushButton(self.frame_2)
        self.loginButton.setGeometry(QtCore.QRect(40, 290, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setKerning(True)
        self.loginButton.setFont(font)
        self.loginButton.setAutoFillBackground(False)
        self.loginButton.setStyleSheet("background-color: rgb(255, 80, 80);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.loginButton.setAutoDefault(False)
        self.loginButton.setDefault(False)
        self.loginButton.setFlat(False)
        self.loginButton.setObjectName("loginButton")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(40, 190, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(65, 65, 65);")
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 917, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
      
        self.loginButton.clicked.connect(self.login)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "Welcome to PASS!"))
        self.label_6.setText(_translate("MainWindow", "Personalized Authentication and Student Surveillance"))
        self.label_7.setText(_translate("MainWindow", "A Face Recognition and Detection System"))
        self.label_8.setText(_translate("MainWindow", "for Real-Time Student Identification."))
        self.usernameText.setPlaceholderText(_translate("MainWindow", "Username"))
        self.label_2.setText(_translate("MainWindow", "Usename"))
        self.label.setText(_translate("MainWindow", "Login"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "********"))
        self.loginButton.setText(_translate("MainWindow", "Login"))
        self.label_3.setText(_translate("MainWindow", "Password"))


    def login(self):
        # Get the entered username and password
        username = self.usernameText.toPlainText()
        password = self.lineEdit.text()

        # Perform database connection and login validation
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='pass_db')
        cursor = db.cursor()

        # Perform the login query
        query = "SELECT * FROM tbl_admin WHERE username=%s AND password=%s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()

        if result:
            # Successful login
            print("Login successful!")
            self.MainWindow.close()
            self.open_dashboard()
        else:
            # Failed login
            print("Invalid username or password")
            dialog = ErrorDialog()
            dialog.setupUi()
            dialog.exec_()

        # Close the database connection
        cursor.close()
        db.close()

    def open_dashboard(self):
        self.MainWindow.hide()
        self.dashboard_window = QtWidgets.QMainWindow()
        self.ui = dashboard.Ui_Dashboard()
        self.ui.setupUi(self.dashboard_window)
        self.ui.tableWidget.setParent(self.ui.centralwidget)
        self.ui.load_logs()
        self.dashboard_window.show()




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

