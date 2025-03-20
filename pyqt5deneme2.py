import sys
from PyQt5 import QtWidgets
class pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.yazi_alani = QtWidgets.QLineEdit()
        self.butun1 = QtWidgets.QPushButton("Yazdir")
        self.buton2 = QtWidgets.QPushButton("Temizle")
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.butun1)
        v_box.addWidget(self.buton2)
        v_box.addStretch()
        self.setLayout(v_box)
        self.setGeometry(250,250,600,600)
        self.butun1.clicked.connect(self.click1)
        self.buton2.clicked.connect(self.click2)
        self.show()

    def click1(self):
        print(self.yazi_alani.text())
    def click2(self):
        self.yazi_alani.clear()

app = QtWidgets.QApplication(sys.argv)
Pencere = pencere()
sys.exit(app.exec_())
