import sys
from PyQt6.QtWidgets import *
from PyQt6 import uic

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("2_7_LineEdit/lineedit.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        #test

        self.lineedit_Test.textChanged.connect(self.lineeditTextFunction)
        self.lineedit_Test.returnPressed.connect(self.printTextFunction)
        self.btn_changeText.clicked.connect(self.changeTextFunction)

    def lineeditTextFunction(self) :
        self.lbl_textHere.setText(self.lineedit_Test.text())

    def printTextFunction(self) :
        print(self.lineedit_Test.text())

    def changeTextFunction(self) :
        self.lineedit_Test.setText("Change Text")


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass() 
    myWindow.show()
    app.exec()