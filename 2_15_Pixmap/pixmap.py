import sys
import urllib.request
from PyQt6.QtWidgets import *
from PyQt6 import uic
from PyQt6.QtGui import *


#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("2_15_Pixmap/pixmap.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        self.btn_loadFromFile.clicked.connect(self.loadImageFromFile)
        self.btn_loadFromWeb.clicked.connect(self.loadImageFromWeb)
        # self.btn_save.clicked.connect(self.saveImageFromWeb)

    def loadImageFromFile(self) :
        #Pixmap 객체 생성
        self.qPixmapFileVar = QPixmap()
        self.qPixmapFileVar.load("C:/Users/cyh51/Pictures/Screenshots/bass.png")
        self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(600)
        self.lbl_picture.setPixmap(self.qPixmapFileVar)

    def loadImageFromWeb(self) :
        urlString = "https://cdn-pro-web-144-135.cdn-nhncommerce.com/wikiwiki1_godomall_com/data/goods/24/12/49/1000011773/1000011773_detail_060.png"
        imageFromWeb = urllib.request.urlopen(urlString).read()
        
        self.qPixmapWebVar = QPixmap()
        self.qPixmapWebVar.loadFromData(imageFromWeb)
        self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(600)
        self.lbl_picture.setPixmap(self.qPixmapWebVar)






if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass() 
    myWindow.show()
    app.exec()