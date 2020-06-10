from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout,QFileDialog,QHBoxLayout,QRadioButton

from PyQt5.QtWidgets import QAction,qApp,QMainWindow
import sys
from PIL import Image,ImageFilter


class Pencere(QWidget):
    def __init__(self):

        super().__init__()

        self.init_ui()

    def init_ui(self):


        self.radio_yazisi = QLabel("Nasıl kırpmak istersin ?")

        self.kare = QRadioButton("Kare")
        self.dik = QRadioButton("Dikdörtgen")

        self.kırp = QPushButton("Kırpmak için tıkla")

        v_box = QVBoxLayout()
        self.setLayout(v_box)

        v_box.addWidget(self.kare)
        v_box.addWidget(self.dik)
        v_box.addWidget(self.kırp)

        self.kırp.clicked.connect(lambda: self.click(self.kare.isChecked(), self.dik.isChecked()))

        self.show()
    def click(self,kare,dik):
        if kare:
            kırpılacak_alan = (0, 0, 270, 310) // Bu ölçüleri kendimiz fotoğrafların boyutuna göre ayarlıyoruz.
        if dik:
            kırpılacak_alan = (0, 0, 240, 400)

        image = Image.open("fotoğraf adresi")
        image.crop(kırpılacak_alan).save("yeni adres")



app = QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())

