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
        self.btn_displayInfo.clicked.connect(self.displayDateTime)
        self.btn_dateTime.clicked.connect(self.enterDateTimeFunc)
        self.btn_date.clicked.connect(self.enterDateFunc)
        self.btn_time.clicked.connect(self.enterTimeFunc)
        self.btn_change.clicked.connect(self.changeFormat)
        self.btn_show.clicked.connect(self.showRangeFunc)
        self.btn_editMax.clicked.connect(self.editMaximum)
        self.btn_editMin.clicked.connect(self.editMinimum)


    def displayDateTime(self) :  
    # DateTimeEdit의 값을 사용할 때는 객체에 값을 저장한 후 사용
    # 사용자가 선택한 값을 꺼내와서 사용하기 위함
    # 가독성, 재사용성, 유지보수
        self.displayDateTimeVar = self.dateTimeEdit_Test.dateTime()
        self.displayDateVar = self.dateTimeEdit_Test.date()
        self.displayTimeVar = self.dateTimeEdit_Test.time()

        # 각 라벨에 값 표시
        self.lbl_displayDateTime.setText(self.displayDateTimeVar.toString("yyyy-MM-dd hh:mm:ss"))
        self.lbl_displayDate.setText(self.displayDateVar.toString("yyyy-MM-dd"))
        self.lbl_displayTime.setText(self.displayTimeVar.toString("hh:mm:ss"))

    # LineEdit에서 가져온 데이터를 QDateTime 객체로 만들고 DateTimeEdit에 적용
    def enterDateTimeFunc(self) :
        self.enterDateTimeText = self.lineEditDateTime.text()
        self.enterDateTimeVar = QDateTime.fromString(self.enterDateTimeText, "yyyy-MM-dd hh:mm:ss")
        self.dateTimeEdit_Test.setDateTime(self.enterDateTimeVar)
    
    def enterDateFunc(self) :
        self.enterDateText = self.lineEditDate.text()
        self.enterDateVar = QDate.fromString(self.enterDateText, "yyyy-MM-dd")
        self.dateTimeEdit_Test.setDate(self.enterDateVar)

    def enterTimeFunc(self) :
        self.enterTimeText = self.lineEditTime.text()
        self.enterTimeVar = QTime.fromString(self.enterTimeText, "hh:mm:ss")
        self.dateTimeEdit_Test.setTime(self.enterTimeVar)

    def changeFormat(self) :
        self.displayFormatText = self.lineEditFormat.text()
        self.dateTimeEdit_Test.setDisplayFormat(self.displayFormatText)

    def showRangeFunc(self) :
        print(self.dateTimeEdit_Test.minimumDateTime())
        print(self.dateTimeEdit_Test.maximumDateTime())

    def editMaximum(self) :
        self.currentMaximumDateTime = self.dateTimeEdit_Test.maximumDateTime()
        self.currentMaximumDateTime = self.currentMaximumDateTime.addDays(10)
        self.dateTimeEdit_Test.setMaximumDateTime(self.currentMaximumDateTime)
    
    def editMinimum(self) :
        self.currentMinimumDateTime = self.dateTimeEdit_Test.minimumDateTime()
        self.currentMinimumDateTime = self.currentMinimumDateTime.addDays(-10)
        self.dateTimeEdit_Test.setMinimumDateTime(self.currentMinimumDateTime)


        

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass() 
    myWindow.show()
    app.exec()



