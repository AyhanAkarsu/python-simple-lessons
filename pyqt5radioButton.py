import sys
from PyQt5 import QtWidgets

class Radiobutton(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.yazi = QtWidgets.QLabel("En sevdiginiz dili secin")
        self.python = QtWidgets.QRadioButton("Python")
        self.java = QtWidgets.QRadioButton("Java")
        self.C = QtWidgets.QRadioButton("C")
        self.buton = QtWidgets.QPushButton("Sec")
        self.yazi_alani = QtWidgets.QLabel("")
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.yazi)
        v_box.addWidget(self.C)
        v_box.addWidget(self.python)
        v_box.addWidget(self.java)
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()
        v_box.addWidget(self.buton)
        self.setLayout(v_box)
        self.setWindowTitle("RadioButton")
        self.buton.clicked.connect(lambda : self.click(self.java.isChecked(),self.C.isChecked(),self.python.isChecked(),self.yazi_alani))
        self.show()

    def click(self,java,c,python,yazi_alani):
        if java:
            yazi_alani.setText("Secim Java...")
        elif c:
            yazi_alani.setText("Secim C...")
        else:
            yazi_alani.setText("Secim Python")

app = QtWidgets.QApplication(sys.argv)
radiobutton = Radiobutton()
sys.exit(app.exec_())
