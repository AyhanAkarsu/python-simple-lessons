import sys
from PyQt5 import QtWidgets

class checkbox(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.checkbox = QtWidgets.QCheckBox("Sec")
        self.buton = QtWidgets.QPushButton("Dene")
        self.yazi_alani = QtWidgets.QLabel("")
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.checkbox)
        v_box.addWidget(self.buton)
        v_box.addWidget(self.yazi_alani)
        self.setLayout(v_box)
        self.setWindowTitle("Checkbox")
        self.buton.clicked.connect(lambda : self.login(self.checkbox.isChecked(),self.yazi_alani))
        self.show()

    def login(self,checkbox,yazi_alani):
        if checkbox:
            yazi_alani.setText("İsaretli..")
        else:
            yazi_alani.setText("İşaretli değil...")



app = QtWidgets.QApplication(sys.argv)
checkboxx = checkbox()
sys.exit(app.exec_())
