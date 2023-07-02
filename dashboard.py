import sys
import os
import register_student
import student_management
import logs
import admin_login
import numpy as np
import pymysql
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (
    QTableWidget,
    QTableWidgetItem,
    QLabel,
)
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from about_dialog import AboutDialog
from PyQt5.QtCore import QTimer
from datetime import datetime, timedelta
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QTableWidget,
    QScrollArea,
)
import openpyxl
from datetime import datetime
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class Ui_Dashboard(object):
    def __init__(self) -> None:
        self.logs_sent = False
        self.existing = False

        # For Excel File
        self.file_name = ""
        self.file_path = ""
        self.folder_name = "logs"
        self.folder_path = rf"C:\Users\SampleUser\Desktop\{self.folder_name}"  # Change this to your own file path

    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setWindowFlags(
            MainWindow.windowFlags()
            & ~QtCore.Qt.WindowMinimizeButtonHint
            & ~QtCore.Qt.WindowMaximizeButtonHint
        )

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # Add table widget
        # self.tableWidget = QTableWidget(self.centralwidget)
        # self.tableWidget.setGeometry(QtCore.QRect(310, 150, 850, 450))
        # self.tableWidget.setObjectName("tableWidget")


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

        self.dashboardBtn = QtWidgets.QPushButton(self.frame)
        self.dashboardBtn.setGeometry(QtCore.QRect(40, 200, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.dashboardBtn.setFont(font)
        self.dashboardBtn.setStyleSheet(
            " background-color: transparent;\n" "color: white;\n" ""
        )
        self.dashboardBtn.setStyleSheet(
            " background-color: transparent;\n"
            "color: white;\n"
            "text-align: left;\n"
            ""
        )
        self.dashboardBtn.setObjectName("dashboardBtn")

        self.logsBtn = QtWidgets.QPushButton(self.frame)
        self.logsBtn.setGeometry(QtCore.QRect(40, 250, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.logsBtn.setFont(font)
        self.logsBtn.setStyleSheet(
            " background-color: transparent;\n" "color: white;\n" ""
        )
        self.logsBtn.setStyleSheet(
            " background-color: transparent;\n"
            "color: white;\n"
            "text-align: left;\n"
            ""
        )
        self.logsBtn.setObjectName("logsBtn")

        self.faceRecognitionBtn = QtWidgets.QPushButton(self.frame)
        self.faceRecognitionBtn.setGeometry(QtCore.QRect(40, 300, 221, 31))
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
        self.registerStudentBtn.setGeometry(QtCore.QRect(40, 350, 221, 31))
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
        self.studentMgmtBtn.setGeometry(QtCore.QRect(40, 400, 221, 31))
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
        self.exitBtn.setGeometry(QtCore.QRect(40, 450, 221, 31))
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
        self.exitBtn_2.setGeometry(QtCore.QRect(40, 500, 221, 31))
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

        self.exportDataBtn = QtWidgets.QPushButton(self.centralwidget)
        self.exportDataBtn.setGeometry(QtCore.QRect(1035, 90, 121, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.exportDataBtn.setFont(font)
        self.exportDataBtn.setObjectName("exportDataBtn")
        self.exportDataBtn.setText("Export Data")
        self.exportDataBtn.clicked.connect(self.export_data_to_excel)

        self.searchComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.searchComboBox.setGeometry(QtCore.QRect(780, 95, 200, 30))
        self.searchComboBox.setObjectName("searchComboBox")
        self.searchComboBox.addItem("CABEIHM")
        self.searchComboBox.addItem("CAS")
        self.searchComboBox.addItem("CICS")
        self.searchComboBox.addItem("CET")
        self.searchComboBox.addItem("CONAHS")
        self.searchComboBox.addItem("CTE")
        self.searchComboBox.addItem("LABORATORY SCHOOL")
        self.searchComboBox.currentTextChanged.connect(self.search_logs)


        self.searchLabel = QtWidgets.QLabel(self.centralwidget)
        self.searchLabel.setGeometry(QtCore.QRect(710, 95, 70, 30))
        self.searchLabel.setObjectName("searchLabel")
        self.searchLabel.setText("Department:")


        #BARCHART
        self.barChart = QtWidgets.QWidget(self.centralwidget)
        self.barChart.setGeometry(QtCore.QRect(385, 180, 700, 400))
        self.barChart.setObjectName("barChart")
        self.barChartLayout = QtWidgets.QVBoxLayout(self.barChart)


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
        self.logsBtn.clicked.connect(self.open_logs)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_9.setText(_translate("MainWindow", "Admin Panel"))
        self.dashboardBtn.setText(_translate("MainWindow", "Dashboard"))
        self.logsBtn.setText(_translate("MainWindow", "Logs"))
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

    # def load_logs(self):

    #     connection = pymysql.connect(
    #         host="localhost", user="root", password="", db="pass_db"
    #     )
    #     cursor = connection.cursor()

    #     delete_query = "DELETE FROM tbl_logs WHERE date_log < %s"
    #     week_ago = datetime.now() - timedelta(days=7)
    #     cursor.execute(delete_query, (week_ago.date(),))
    #     connection.commit()

    #     query = "SELECT  tbl_student.image, tbl_student.first_name, tbl_student.last_name, tbl_student.course, tbl_student.sr_code, tbl_logs.date_log, tbl_logs.time_log, tbl_logs.log_type FROM tbl_logs LEFT JOIN tbl_student ON tbl_logs.student_id = tbl_student.id"
    #     cursor.execute(query)
    #     logs = cursor.fetchall()

    #     row_count = len(logs)
    #     column_count = 8  # Increase the column count for the image column

    #     self.tableWidget.setRowCount(row_count)
    #     self.tableWidget.setColumnCount(column_count)

    #     header_labels = [
    #         "Image",
    #         "First Name",
    #         "Last Name",
    #         "Course",
    #         "SR Code",
    #         "Date Log",
    #         "Time Log",
    #         "Log Type",
    #     ]
    #     self.tableWidget.setHorizontalHeaderLabels(header_labels)

    #     for row, log in enumerate(logs):
    #         (
    #             image_filename,
    #             first_name,
    #             last_name,
    #             course,
    #             sr_code,
    #             date_log,
    #             time_log,
    #             log_type,
    #         ) = log

    #         # Create a QLabel and set the image pixmap
    #         image_label = QLabel()
    #         image_path = os.path.join("images", str(image_filename))
    #         pixmap = QPixmap(image_path)
    #         if not pixmap.isNull():
    #             # Calculate the size of the cell
    #             cell_width = self.tableWidget.columnWidth(0)
    #             cell_height = self.tableWidget.rowHeight(row)

    #             # Resize the pixmap to fit the cell dimensions
    #             scaled_pixmap = pixmap.scaled(
    #                 cell_width, cell_height, Qt.AspectRatioMode.KeepAspectRatio
    #             )

    #             # Set the scaled pixmap on the image label
    #             image_label.setPixmap(scaled_pixmap)
    #             image_label.setAlignment(
    #                 Qt.AlignCenter
    #             )  # Center the image in the label

    #         self.tableWidget.setCellWidget(row, 0, image_label)

    #         self.tableWidget.setItem(row, 1, QTableWidgetItem(first_name))
    #         self.tableWidget.setItem(row, 2, QTableWidgetItem(last_name))
    #         self.tableWidget.setItem(row, 3, QTableWidgetItem(course))
    #         self.tableWidget.setItem(row, 4, QTableWidgetItem(sr_code))

    #         self.tableWidget.setItem(row, 5, QTableWidgetItem(str(date_log)))
    #         self.tableWidget.setItem(row, 6, QTableWidgetItem(str(time_log)))
    #         self.tableWidget.setItem(row, 7, QTableWidgetItem(log_type))

    #     cursor.close()

        # Schedule the next update after 1 second
        # QTimer.singleShot(1000, self.load_logs)


    def start_loading_students(self):
        # Start loading the students initially
        # self.load_logs()
        print("Load Students")


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


    def open_logs(self):
        print("Opening Logs...")
        self.MainWindow.hide()
        self.logs_window = QtWidgets.QMainWindow()
        self.ui = logs.Logs()
        self.ui.setupUi(self.logs_window)
        self.ui.tableWidget.setParent(self.ui.centralwidget)
        self.ui.load_logs()
        self.logs_window.show()


    def search_logs(self):
        selected_department = self.searchComboBox.currentText()

        # Connect to the MySQL database
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='pass_db'
        )

        try:
            # Execute the query and fetch the age and gender data
            cursor = connection.cursor()
            query = f"SELECT age, COUNT(tbl_logs.id) AS count FROM tbl_student LEFT JOIN tbl_logs ON tbl_logs.student_id = tbl_student.id WHERE department = '{selected_department}' GROUP BY age"
            cursor.execute(query)
            ages = []
            male_counts = []
            female_counts = []
            for row in cursor.fetchall():
                age, count = row
                ages.append(age)
                if age == 'Male':
                    female_counts.append(int(count))
                    female_counts.append(0)
                else:
                    male_counts.append(0)
                    male_counts.append(int(count))

            for i in reversed(range(self.barChartLayout.count())):
                self.barChartLayout.itemAt(i).widget().setParent(None)

            if ages and (male_counts or female_counts):
                fig, ax = plt.subplots()
                width = 0.35
                male_bar = ax.bar(ages, male_counts, width, label='Male')
                female_bar = ax.bar(ages, female_counts, width, bottom=male_counts, label='Female')
                ax.set_xlabel(selected_department)
                ax.set_ylabel('Log Count')
                ax.set_title('')
                ax.tick_params(axis='x')
                ax.set_xticks(ages)
                ax.legend()

                canvas = FigureCanvas(fig)
                self.barChartLayout.addWidget(canvas)
                canvas.draw()

        finally:
            connection.close()

    def export_data_to_excel(self):
        # Connect to the MySQL database
        connection = pymysql.connect(
            host="localhost", user="root", password="", database="pass_db"
        )

        try:
            # Create a cursor object to execute SQL queries
            cursor = connection.cursor()

            # Retrieve data from the tbl_student table
            select_query = "SELECT CONCAT(tbl_student.first_name, ' ', tbl_student.last_name) AS student_name, tbl_student.course, tbl_student.sr_code, tbl_logs.date_log, tbl_logs.time_log FROM tbl_logs LEFT JOIN tbl_student ON tbl_logs.student_id = tbl_student.id"
            cursor.execute(select_query)
            student_data = cursor.fetchall()

            # Create a new Excel workbook and select the active sheet
            workbook = openpyxl.Workbook()
            sheet = workbook.active

            # Write the column headers
            sheet["A1"] = "Student Name"
            sheet["B1"] = "Course"
            sheet["C1"] = "SR Code"
            sheet["D1"] = "Date Log"
            sheet["E1"] = "Time Log"

            # Set column width for date columns
            date_columns = ["D", "E"]  # Columns D and E represent the date columns
            for column in date_columns:
                sheet.column_dimensions[
                    column
                ].width = 15  # Adjust the width as per your preference

            for row_index, student in enumerate(student_data, start=2):
                sheet.cell(row=row_index, column=1).value = student[0]
                sheet.cell(row=row_index, column=2).value = student[1]
                sheet.cell(row=row_index, column=3).value = student[2]
                sheet.cell(row=row_index, column=4).value = student[3]
                sheet.cell(row=row_index, column=5).value = student[4]

            # Save the Excel file
            current_datetime = datetime.now()
            formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
            self.file_name = f"logs_data_{formatted_datetime}.xlsx"

            # Save the Excel file inside the "folder_path" folder
            self.file_path = rf"{self.folder_path}\{self.file_name}"

            # Create the "logs" folder if it doesn't exist
            if not os.path.exists(self.folder_path):
                os.makedirs(self.folder_path)
            # Save the Excel file
            workbook.save(self.file_path)
            print("Logs Data exported to Excel successfully!")

        except Exception as e:
            print("Error exporting data to Excel:", str(e))

        finally:
            # Close the cursor and connection
            cursor.close()
            connection.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Dashboard()
    ui.setupUi(MainWindow)
    # ui.load_logs()
    MainWindow.show()
    sys.exit(app.exec_())
