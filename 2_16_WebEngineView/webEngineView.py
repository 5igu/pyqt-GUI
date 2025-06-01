import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6 import uic
from PyQt6.QtWebEngineWidgets import QWebEngineView

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("2_16_WebEngineView/webEngineView.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        self.webEngineView_Test.loadStarted.connect(self.printLoadStart)
        self.webEngineView_Test.loadProgress.connect(self.printLoading)
        self.webEngineView_Test.loadFinished.connect(self.printLoadFinished)
        self.webEngineView_Test.urlChanged.connect(self.urlChangedFunction)

        # button
        self.btn_setUrl.clicked.connect(self.urlGo)
        self.btn_back.clicked.connect(self.btnBackFunc)
        self.btn_forward.clicked.connect(self.btnForwardFunc)
        self.btn_reload.clicked.connect(self.btnReloadFunc)
        self.btn_stop.clicked.connect(self.btnStopFunc)
        


    # webEngineView 연결 함수
    def printLoadStart(self) : print("Start Loading")
    def printLoading(self) : print("Loading")
    def printLoadFinished(self) : print("Load Finished")


    def urlChangedFunction(self) :
        self.line_url.setText(self.webEngineView_Test.url().toString())
        print("Url Changed")




    # 버튼 클릭 기능
    def urlGo(self) :
        self.webEngineView_Test.load(QUrl(self.line_url.text()))

    def btnBackFunc(self) :
        self.webEngineView_Test.back()

    def btnForwardFunc(self) :
        self.webEngineView_Test.forward()

    def btnReloadFunc(self) :
        self.webEngineView_Test.reload()

    def btnStopFunc(self) :
        self.webEngineView_Test.stop()


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass() 
    myWindow.show()
    app.exec()