


import sys
from PyQt6.QtWidgets import *
from PyQt6 import uic

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("2_18_ListWidget/listWidget.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        # ListWidget 시그널
        self.listWidget_Test.itemClicked.connect(self.chkItemClicked)
        self.listWidget_Test.itemDoubleClicked.connect(self.chkItemDoubleClicked)
        self.listWidget_Test.currentItemChanged.connect(self.chkCurrentItemChanged)

    
    
    # List Widget 시그널 함수
    def chkItemClicked(self) :  
        # 1st Item
        print(self.listWidget_Test.currentItem().text())
    
    def chkItemDoubleClicked(self) : 
        # 1st Item 
        # 0 : 1st Item
        print(str(self.listWidget_Test.currentRow()) + " : " + self.listWidget_Test.currentItem().text())
    
    def chkCurrentItemChanged(self) :
        # Current Row : 0
        print("Current Row : " + str(self.listWidget_Test.currentRow()))

    # List Widget 항목 함수
    def addListWidget(self) :
        self.addItemText = self.line_addItem.text()
        self.listWidget_Test.addItem(self.addItemText)

    def insertListWidget(self) :
        self.insertRow = self.spin_insertRow.value()
        self.insertText = self.line_insertItem.text()
        self.listWidget_Test.insertItem(self.insertRowm, self.insertText)



if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass() 
    myWindow.show()
    app.exec()