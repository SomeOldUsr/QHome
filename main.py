from PyQt5 import QtWidgets, uic
import PyQt5
import sys


class Ui(QtWidgets.QMainWindow):

    # optional type hints
    pushButton: PyQt5.QtWidgets.QPushButton
    pushButton_2: PyQt5.QtWidgets.QPushButton

    def __init__(self, path):
        super(Ui, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi(path, self)  # Load the .ui file

        # adding a clicked event
        self.pushButton.clicked.connect(self.mes)
        self.pushButton_2.clicked.connect(self.mes)

        # show window
        self.show()

    def mes(self):
        QtWidgets.QMessageBox(text=self.sender().text()).exec()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui('UI/Klingel.ui')
    app.exec_()
