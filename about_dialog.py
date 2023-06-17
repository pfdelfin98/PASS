from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QPushButton, QDesktopWidget, QMessageBox
from PyQt5.QtCore import QTimer

class AboutDialog(QDialog):
    def setupUi(self):        
        self.setWindowTitle("About Us")
        self.setGeometry(0, 0, 300, 150)  # Set initial geometry to (0, 0, 300, 150)

        message_box = QMessageBox(self)
        message_box.setIcon(QMessageBox.Information)
        message_box.setWindowTitle("About Us")

        message_text = "<p>Welcome to PASS!</p>"
        message_text += "<p>We are a team of developers dedicated to creating innovative software solutions.</p>"
        message_text += "<p>Thank you for using our application.</p>"
        message_box.setText(message_text)

        message_box.setStandardButtons(QMessageBox.Ok)
        message_box.setDefaultButton(QMessageBox.Ok)
        message_box.buttonClicked.connect(self.close)

        self.center_dialog()
        message_box.exec_()

    def center_dialog(self):
        screen_geo = QDesktopWidget().screenGeometry()
        dialog_geo = self.geometry()
        center_pos = screen_geo.center() - dialog_geo.center()
        self.move(center_pos)

if __name__ == "__main__":
    app = QApplication([])
    dialog = AboutDialog()
    dialog.setupUi()
    dialog.exec_()
