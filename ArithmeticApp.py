from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import *
import sys
from ArithmeticUI import *

class Naveen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.addB.clicked.connect(self.addition)
        self.ui.subB.clicked.connect(self.subtraction)
        self.ui.mulB.clicked.connect(self.multiplication)
        self.ui.divB.clicked.connect(self.division)
    def addition(self):
        x = float(self.ui.a.text())
        y = float(self.ui.b.text())
        self.ui.result.setText("Addition = {}".format(x+y))
        
    def subtraction(self):
        x = float(self.ui.a.text())
        y = float(self.ui.b.text())
        self.ui.result.setText("Subtraction = {}".format(x-y))
    def multiplication(self):
        x = float(self.ui.a.text())
        y = float(self.ui.b.text())
        self.ui.result.setText("Multiplication = {}".format(x*y))
    def division(self):
        x = float(self.ui.a.text())
        y = float(self.ui.b.text())
        self.ui.result.setText("Division = {:.3f}".format(x/y))



if __name__=="__main__":
    app = QApplication(sys.argv)
    w = Naveen()
    w.show()
    sys.exit(app.exec_())

