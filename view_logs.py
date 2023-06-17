import sys
import os
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem, QApplication, QDialog, QLabel, QPushButton, QDesktopWidget
import pymysql

class ViewLogsDialog(QDialog):
    def setupUi(self, student_id):
        self.student_id = student_id

        self.setWindowTitle("View Logs")
        self.setGeometry(700, 300, 500, 300)

        # Create a QTableWidget to display the logs
        self.logsTable = QTableWidget(self)
        self.logsTable.setGeometry(20, 20, 460, 260)
        self.logsTable.setColumnCount(3)
        self.logsTable.setHorizontalHeaderLabels(["Student Name", "Date Log", "Time Log"])

        # Connect to the MySQL database
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='pass_db'
        )

        try:
            # Create a cursor object to execute SQL queries
            cursor = connection.cursor()

            # Fetch logs data from the database joined with tbl_student to get student name
            query = "SELECT CONCAT(tbl_student.first_name, ' ', tbl_student.last_name) AS student_name, tbl_logs.date_log, tbl_logs.time_log " \
                    "FROM tbl_logs " \
                    "LEFT JOIN tbl_student ON tbl_student.id = tbl_logs.student_id " \
                    "WHERE tbl_logs.student_id = %s"
            cursor.execute(query, (self.student_id,))
            logs = cursor.fetchall()

            # Set the row count for the table
            self.logsTable.setRowCount(len(logs))

            # Fill in the table with the retrieved logs
            for row, log in enumerate(logs):
                student_name_item = QTableWidgetItem(log[0])
                date_log_item = QTableWidgetItem(str(log[1]))
                time_log_item = QTableWidgetItem(str(log[2]))

                self.logsTable.setItem(row, 0, student_name_item)
                self.logsTable.setItem(row, 1, date_log_item)
                self.logsTable.setItem(row, 2, time_log_item)

            # Resize the columns to fit the content
            self.logsTable.resizeColumnsToContents()

        except Exception as e:
            print("Error fetching logs:", str(e))

        finally:
            # Close the cursor and connection
            cursor.close()
            connection.close()

    def center_dialog(self):
        screen_geo = QDesktopWidget().screenGeometry()
        dialog_geo = self.geometry()
        center_pos = screen_geo.center() - dialog_geo.center()
        self.move(center_pos)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = ViewLogsDialog()
    dialog.setupUi(1)  # Pass the student ID here for testing
    dialog.center_dialog()  # Center the dialog on the screen
    dialog.exec_()
    sys.exit(app.exec_())
