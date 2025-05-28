# Rich Text: 글자의 색상, 크기, 기울임, 굵기 등 조절 가능한 텍스트
# Plain Text: 색상, 크기를 조절할 수 없고 시스템에서 지정된대로만 글자를 표시

# PlainTextEdit은 Plain Text를 지원하는 글자 입력 위젯
# LineEdit과 다르게 여러 줄의 데이터 입력 가능
# LineEdit처럼 위젯 더블클릭으로 미리 값을 입력할 수도 있음



import sys
from PyQt6.QtWidgets import *
from PyQt6 import uic

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("2_8_TextEdit+PlainTextEdit/plaintextedit.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        #test

        self.btn_printPTE.clicked.connect(self.printPTE)
        self.btn_clearPTE.clicked.connect(self.clearPTE)
        self.btn_appendPT.clicked.connect(self.appendPT)

    def printPTE(self) :
        print(self.plainTextEdit_Test.toPlainText())
    
    def clearPTE(self) :
        self.plainTextEdit_Test.clear()

    def appendPT(self) :
        self.plainTextEdit_Test.appendPlainText("Append Plain Text")









if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass() 
    myWindow.show()
    app.exec()