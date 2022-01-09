from PyQt5 import QtWidgets as qt
from PyQt5 import QtGui as gui
from PYQT5_Validate_Email_ui import Ui_Window1 as ui
import sys,re

class Window(qt.QMainWindow):


    def __init__(self):
        super(Window, self).__init__()

        self.ui = ui()
        self.ui.setupUi(self)

        self.ui.btnValidate.clicked.connect(self.validateEmail)
        self.ui.btnClear.clicked.connect(self.clearFields)


    def validateEmail(self):

        email = self.ui.txtEmail.text()
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        if (re.fullmatch(regex, email)) :
            msg1 = qt.QMessageBox()
            msg1.setIcon(qt.QMessageBox.Information)
            msg1.setText("Provided email is Valid.")
            msg1.setWindowTitle("Information MessageBox")
            msg1.setStandardButtons(qt.QMessageBox.Ok)
            msg1.exec_()     
        else :
            msg2 = qt.QMessageBox()
            msg2.setIcon(qt.QMessageBox.Warning)
            msg2.setText("Provided email is not valid !")
            msg2.setWindowTitle("Information MessageBox")
            msg2.setStandardButtons(qt.QMessageBox.Ok)
            msg2.exec_()   

    def clearFields(self) :

        self.ui.txtEmail.setText("")


# Run Application

app = qt.QApplication([])
application = Window()
application.show()

app.exec()