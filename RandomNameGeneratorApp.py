import sys
from random import *
from datetime import date
from PyQt5.QtWidgets import QMainWindow,QApplication
from RandomNameGeneratorUI import *


class MyForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.nameGenerator)
        self.ui.pushButton_2.clicked.connect(self.exit)
        
    def nameGenerator(self):
        file = open("names.txt", "r")
        l=[]
        for i in file:
            l.append(i.strip('\n'))

        self.ui.label_2.setText(choice(l))
        file.close()
        
    def exit(self):
        
        sys.exit()
        

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
