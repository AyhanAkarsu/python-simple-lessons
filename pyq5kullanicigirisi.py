from PyQt5 import QtWidgets
import sys
import sqlite3
class kullanici(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.baglanti()

    def init_ui(self):
        self.id = QtWidgets.QLineEdit()
        self.parola = QtWidgets.QLineEdit()
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.buton = QtWidgets.QPushButton("Giris Yap")
        self.yazi_alani = QtWidgets.QLabel("")
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.id)
        v_box.addWidget(self.parola)
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()
        v_box.addWidget(self.buton)
        self.setWindowTitle("Kullanici Girisi")
        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()
        self.buton.clicked.connect(self.login)
        self.setLayout(h_box)
        self.show()

    def baglanti(self):
        self.baglan = sqlite3.connect("Uyelikdata.db")
        self.cursor = self.baglan.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS uyelik (isim TEXT,parola TEXT)")
        self.baglan.commit()
    def login(self):
        ad = self.id.text()
        par = self.parola.text()
        self.cursor.execute("Select * From uyelik where isim = ? and parola = ?",(ad,par))
        data = self.cursor.fetchall()
        if len(data) == 0:
           self.yazi_alani.setText("Yanlış giriş yapdiniz..\nTekrar deneyiniz..")
        else:
            self.yazi_alani.setText("Hoşgeldiniz: "+ad)


app = QtWidgets.QApplication(sys.argv)
Kullanici = kullanici()
sys.exit(app.exec_())