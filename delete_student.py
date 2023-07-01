import sys
import os
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QPushButton, QDesktopWidget
import pymysql
from encodegenerator import encodegenerator


class DeleteStudentDialog(QDialog):
    def setupUi(self, student_id):
        self.student_id = student_id

        self.setWindowTitle("Delete Student")
        self.setGeometry(700, 300, 300, 150)

        self.confirmationLabel = QLabel(
            "Are you sure you want to delete this student?", self
        )
        self.confirmationLabel.setGeometry(20, 20, 260, 30)

        self.confirmButton = QPushButton("Confirm", self)
        self.confirmButton.setGeometry(100, 70, 100, 30)
        self.confirmButton.clicked.connect(self.confirm_delete)

    def confirm_delete(self):
        # Connect to the MySQL database
        connection = pymysql.connect(
            host="localhost", user="root", password="", database="pass_db"
        )

        try:
            # Create a cursor object to execute SQL queries
            cursor = connection.cursor()

            # Get the student details from the database before deleting
            select_query = (
                "SELECT first_name, last_name, image FROM tbl_student WHERE id = %s"
            )
            cursor.execute(select_query, (self.student_id,))
            student_data = cursor.fetchone()

            if student_data:
                # Extract the student details
                first_name, last_name, image_path = student_data

                # Delete the student from the database where id = student_id
                delete_query = "DELETE FROM tbl_student WHERE id = %s"
                cursor.execute(delete_query, (self.student_id,))

                # Delete all student logs from the database
                delete_logs_query = "DELETE FROM tbl_logs WHERE student_id = %s"
                cursor.execute(delete_logs_query, (self.student_id,))

                # Commit the changes to the database
                connection.commit()

                print("Student deleted successfully!")

                # Delete the image file if it exists
                if image_path:
                    image_filename = f"{first_name}-{last_name}-{self.student_id}{os.path.splitext(image_path)[1]}"
                    image_save_path = f"images/{image_filename}"  # Change 'images' to your desired folder path

                    if os.path.exists(image_save_path):
                        os.remove(image_save_path)
                        print("Image file deleted successfully!")

            else:
                print("Student not found in the database.")

        except Exception as e:
            print("Error deleting student:", str(e))
            connection.rollback()

        finally:
            # Close the cursor and connection
            cursor.close()
            connection.close()
            encodegenerator()

        # Close the dialog
        self.close()

    def center_dialog(self):
        screen_geo = QDesktopWidget().screenGeometry()
        dialog_geo = self.geometry()
        center_pos = screen_geo.center() - dialog_geo.center()
        self.move(center_pos)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = DeleteStudentDialog()
    dialog.setupUi(1)  # Pass the student ID here for testing
    dialog.center_dialog()  # Center the dialog on the screen
    dialog.exec_()
    sys.exit(app.exec_())
