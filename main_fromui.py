from PyQt5 import QtWidgets, uic
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('main_window.ui', self) # Load the .ui file
        self.show() # Show the GUI

        # finding the widgets
        self.btn_text_info = self.findChild(QtWidgets.QPushButton, "btn_text_info")
        self.btn_visualize = self.findChild(QtWidgets.QPushButton, "btn_visualize")
        self.btn_preprocess = self.findChild(QtWidgets.QPushButton, "btn_preprocess")


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()