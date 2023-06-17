from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QPushButton, QDesktopWidget, QMessageBox
from PyQt5.QtCore import QTimer

class ErrorImageDialog(QDialog):
    def setupUi(self):        
        self.setWindowTitle("Error Dialog")
        self.setGeometry(700, 300, 300, 150)

        self.errorLabel = QLabel("Image format not supported please select .jpg image", self)
        self.errorLabel.setGeometry(30, 20, 260, 30)
        self.errorLabel.setStyleSheet("QLabel { color: black; text-align: center; }") 

        self.confirmButton = QPushButton("OK", self)
        self.confirmButton.setGeometry(100, 70, 100, 30)
        self.confirmButton.clicked.connect(self.close) 

        self.timer = QTimer(self)  
        self.timer.setSingleShot(True)  
        self.timer.timeout.connect(self.close)  
        self.timer.start(3000) 

    def center_dialog(self):
        screen_geo = QDesktopWidget().screenGeometry()
        dialog_geo = self.geometry()
        center_pos = screen_geo.center() - dialog_geo.center()
        self.move(center_pos)

if __name__ == "__main__":
    app = QApplication([])
    dialog = ErrorImageDialog()
    dialog.setupUi()
    dialog.center_dialog()
    dialog.exec_()
