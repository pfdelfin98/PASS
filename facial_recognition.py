import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow

from PyQt5 import QtCore, QtWidgets

class FacialRecognitionWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow 
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1186, 647)
        self.imageFilePath = None
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-1, 1, 261, 691))
    


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = FacialRecognitionWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
