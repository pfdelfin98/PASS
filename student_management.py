import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
import pymysql

class StudentManagementWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow 
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1186, 647)
        self.imageFilePath = None
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-1, 1, 261, 691))

        # Create the table widget
        self.table_widget = QtWidgets.QTableWidget(self.centralwidget)
        self.table_widget.setGeometry(QtCore.QRect(260, 0, 931, 591))
        self.table_widget.setObjectName("table_widget")
        self.table_widget.setColumnCount(5)
        self.table_widget.setHorizontalHeaderLabels(["First Name", "Middle Name", "Last Name", "Course", "Actions"])
        self.table_widget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_widget.cellClicked.connect(self.handle_table_button_click)

        # Add data to the table
        self.populate_table()

        # Set the central widget of the main window
        MainWindow.setCentralWidget(self.centralwidget)

    def populate_table(self):
        # Connect to the database
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="pass_db"
        )

        try:
            # Create a cursor object
            cursor = connection.cursor()

            # Execute the SQL query to fetch student information
            query = "SELECT first_name, middle_name, last_name, course FROM tbl_student"
            cursor.execute(query)

            # Fetch all rows from the result set
            rows = cursor.fetchall()

            # Set the number of rows in the table widget
            self.table_widget.setRowCount(len(rows))

            # Populate the table widget with student information
            for row_index, row_data in enumerate(rows):
                for col_index, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    self.table_widget.setItem(row_index, col_index, item)

        finally:
            # Close the cursor and connection
            cursor.close()
            connection.close()

    def handle_table_button_click(self, row, column):
        if column == 4:  # Actions column
            button = self.table_widget.cellWidget(row, column)
            if button.text() == "Update":
                self.update_student(row)
            elif button.text() == "Delete":
                self.delete_student(row)

    def update_student(self, row):
        first_name_item = self.table_widget.item(row, 0)
        middle_name_item = self.table_widget.item(row, 1)
        last_name_item = self.table_widget.item(row, 2)
        course_item = self.table_widget.item(row, 3)

        if first_name_item and middle_name_item and last_name_item and course_item:
            first_name = first_name_item.text()
            middle_name = middle_name_item.text()
            last_name = last_name_item.text()
            course = course_item.text()

            # Perform the update operation based on the retrieved information
            # Add your code here to update the student in the database
            print(f"Updating student: {first_name} {middle_name} {last_name} - Course: {course}")


    def delete_student(self, row):
        # Retrieve the student information from the selected row in the table widget
        table_widget = self.centralWidget().findChild(QtWidgets.QTableWidget)
        first_name = table_widget.item(row, 0).text()
        middle_name = table_widget.item(row, 1).text()
        last_name = table_widget.item(row, 2).text()
        course = table_widget.item(row, 3).text()

        # Perform the delete operation based on the retrieved information
        # Add your code here to delete the student from the database
        print(f"Deleting student: {first_name} {middle_name} {last_name} - Course: {course}")

        # Perform the delete operation based on the retrieved information
        # Add your code here to delete the student from the database


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = StudentManagementWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
