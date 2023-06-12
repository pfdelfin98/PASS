from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog
from PyQt5.QtGui import QPixmap
import sys
import pymysql
import os
from encodegenerator import encodegenerator

class EditStudentDialog(QDialog):
    def setupUi(self, student_id):
        self.student_id = student_id
        self.setWindowTitle("Edit Student")
        self.layout = QVBoxLayout()

        # Add labels and text boxes for first name, middle name, and last name
        self.label_first_name = QLabel("First Name:")
        self.layout.addWidget(self.label_first_name)

        self.text_box_first_name = QLineEdit()
        self.layout.addWidget(self.text_box_first_name)

        self.label_middle_name = QLabel("Middle Name:")
        self.layout.addWidget(self.label_middle_name)

        self.text_box_middle_name = QLineEdit()
        self.layout.addWidget(self.text_box_middle_name)

        self.label_last_name = QLabel("Last Name:")
        self.layout.addWidget(self.label_last_name)

        self.text_box_last_name = QLineEdit()
        self.layout.addWidget(self.text_box_last_name)

        # Add an image label and a button to upload an image
        self.label_image = QLabel()
        self.layout.addWidget(self.label_image)

        self.button_upload_image = QPushButton("Upload Image")
        self.button_upload_image.clicked.connect(self.upload_image)
        self.layout.addWidget(self.button_upload_image)

        # Add a button to save the changes
        self.button_save_changes = QPushButton("Save Changes")
        self.button_save_changes.clicked.connect(self.save_changes)
        self.layout.addWidget(self.button_save_changes)

        self.setLayout(self.layout)

        # Retrieve and populate the student data
        self.retrieve_student_data()

    def retrieve_student_data(self):
        # Connect to MySQL and retrieve student details
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='pass_db'
        )
        cursor = connection.cursor()

        # Retrieve student details using the student ID
        query = "SELECT first_name, middle_name, last_name, image FROM tbl_student WHERE id = %s"
        cursor.execute(query, (self.student_id,))
        student_data = cursor.fetchone()

        if student_data:
            first_name, middle_name, last_name, image = student_data
            self.text_box_first_name.setText(first_name)
            self.text_box_middle_name.setText(middle_name)
            self.text_box_last_name.setText(last_name)

            if image:
                image_path = f"images/{image}"
                self.display_image(image_path)

        else:
            print("Student not found.")

        cursor.close()
        connection.close()

    def upload_image(self):
        file_dialog = QFileDialog()
        image_path, _ = file_dialog.getOpenFileName(self, 'Upload Image', '', 'Image Files (*.png *.jpg *.jpeg)')

        if image_path:
            self.display_image(image_path)

    def display_image(self, image_path):
        pixmap = QPixmap(image_path)
        self.label_image.setPixmap(pixmap.scaledToWidth(300))  # Adjust the width as needed

    def save_changes(self):
        # Add code to save the changes made to the student
        first_name = self.text_box_first_name.text()
        middle_name = self.text_box_middle_name.text()
        last_name = self.text_box_last_name.text()
        print("Saving changes for Student ID:", self.student_id)
        print("Updated first name:", first_name)
        print("Updated middle name:", middle_name)
        print("Updated last name:", last_name)

        # Connect to MySQL and update student details
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='pass_db'
        )
        cursor = connection.cursor()

        # Retrieve the original student details
        query = "SELECT first_name, middle_name, last_name, image FROM tbl_student WHERE id = %s"
        cursor.execute(query, (self.student_id,))
        original_student_data = cursor.fetchone()

        if original_student_data:
            original_first_name, original_middle_name, original_last_name, original_image = original_student_data

            # Check if the first name or last name has changed
            if original_first_name != first_name or original_last_name != last_name:
                # Check if the old image file exists
                old_image_filename = f"{original_first_name}-{original_last_name}-{self.student_id}.jpg"
                old_image_path = f"images/{old_image_filename}"

                if os.path.exists(old_image_path):
                    # Generate new image filename
                    new_image_filename = f"{first_name}-{last_name}-{self.student_id}.jpg"
                    new_image_path = f"images/{new_image_filename}"

                    # Rename the old image file to the new name
                    os.rename(old_image_path, new_image_path)

                    # Update the student record with the new image filename
                    update_query = "UPDATE tbl_student SET image = %s WHERE id = %s"
                    update_values = (new_image_filename, self.student_id)
                    cursor.execute(update_query, update_values)
                    connection.commit()
                    print("Image file renamed and updated in the database.")

            # Check if a new image has been uploaded
            if self.label_image.pixmap() and self.label_image.pixmap().toImage().isNull() == False:
                new_image_filename = f"{first_name}-{last_name}-{self.student_id}.jpg"
                new_image_path = f"images/{new_image_filename}"

                # Save the uploaded image
                self.label_image.pixmap().save(new_image_path)

                # Update the student record with the new image filename
                update_query = "UPDATE tbl_student SET image = %s WHERE id = %s"
                update_values = (new_image_filename, self.student_id)
                cursor.execute(update_query, update_values)
                connection.commit()
                print("Image file saved and updated in the database.")

        # Update other student details
        update_query = "UPDATE tbl_student SET first_name = %s, middle_name = %s, last_name = %s WHERE id = %s"
        update_values = (first_name, middle_name, last_name, self.student_id)
        cursor.execute(update_query, update_values)
        connection.commit()
        print("Student details updated in the database.")

        encodegenerator()
        cursor.close()
        connection.close()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = EditStudentDialog()
    dialog.setupUi(1)  # Pass the student ID here for testing
    dialog.exec_()
    sys.exit(app.exec_())

