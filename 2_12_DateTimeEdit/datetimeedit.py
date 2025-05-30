import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *  ## QDateTime
from PyQt6 import uic

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("2_12_DateTimeEdit/datetimeedit.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
    
        # DateTimeEdit의 디폴트 값을 현재 날짜로 설정
        self.currentDateTime = QDateTime.currentDateTime()
        self.dateTimeEdit_Test.setDateTime(self.currentDateTime)

        # button
        self.btn_displayDateTime.clicked.connect(self.displayDateTime)


    def displayDateTime(self) :  
    # DateTimeEdit의 값을 사용할 때는 객체에 값을 저장한 후 사용
    # 사용자가 선택한 값을 꺼내와서 사용하기 위함
    # 가독성, 재사용성, 유지보수
        self.displayDateTimeVar = self.dateTimeEdit_Test.dateTime()
        self.lbl_displayDateTime.setText(self.displayDateTimeVar.toString("yyyy-MM-dd AP hh:mm:ss"))



if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass() 
    myWindow.show()
    app.exec()