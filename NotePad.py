from PyQt5 import QtWidgets
import sys

class notepad(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.temizle = QtWidgets.QPushButton("Temizle")
        self.ac = QtWidgets.QPushButton("Ac")
        self.kaydet = QtWidgets.QPushButton("Kaydet")
        self.yazi_alani = QtWidgets.QTextEdit()
        self.h_box = QtWidgets.QHBoxLayout()
        self.h_box.addWidget(self.temizle)
        self.h_box.addWidget(self.ac)
        self.h_box.addWidget(self.kaydet)
        self.v_box = QtWidgets.QVBoxLayout()
        self.v_box.addWidget(self.yazi_alani)
        self.v_box.addLayout(self.h_box)
        self.setLayout(self.v_box)
        self.setWindowTitle("MYNotePad")
        self.setGeometry(450, 100, 900, 900)
        self.temizle.clicked.connect(self.f_temizle)
        self.ac.clicked.connect(self.f_ac)
        self.kaydet.clicked.connect(self.f_kaydet)
        self.show()
    def f_temizle(self):
        self.yazi_alani.clear()
    def f_ac(self):
        dosya = QtWidgets.QFileDialog.getOpenFileName(self, "Dosya Ac")
        with open(dosya[0], "r") as file:
            self.yazi_alani.setText(file.read())
    def f_kaydet(self):
        dosya = QtWidgets.QFileDialog.getSaveFileName(self, "Dosya Kaydet")
        with open(dosya[0], "w") as file:
            file.write(self.yazi_alani.toPlainText())


app = QtWidgets.QApplication(sys.argv)
NotePad = notepad()
sys.exit(app.exec_())
