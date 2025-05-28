import sys
from PyQt6.QtWidgets import *
from PyQt6 import uic

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("2_6_TextBrowser/textbrowser.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        #test

        #버튼에 기능을 할당하는 코드
        self.btn_Print.clicked.connect(self.printTextFunction)
        self.btn_setText.clicked.connect(self.changeTextFunction)
        self.btn_appendText.clicked.connect(self.appendTextFunction)
        self.btn_Clear.clicked.connect(self.clearTextFunction)

    def printTextFunction(self) :
        #self.Textbrowser이름.toPlainText()
        #Textbrowser에 있는 글자를 가져오는 메서드
        print(self.textbrow_Test.toPlainText())


    def changeTextFunction(self) :
        #self.Textbrowser이름.setPlainText()
        #Textbrowser에 있는 글자를 가져오는 메서드
        self.textbrow_Test.setPlainText("This is Textbrowser - Change Text")

    def appendTextFunction(self) :
        #self.Textbrowser이름.append()
        #Textbrowser에 있는 글자를 가져오는 메서드
        self.textbrow_Test.append("Append Text")

    def clearTextFunction(self) :
        #self.Textbrowser.clear()
        #Textbrowser에 있는 글자를 지우는 메서드
        self.textbrow_Test.clear()


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass() 
    myWindow.show()
    app.exec()