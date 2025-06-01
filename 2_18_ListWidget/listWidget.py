


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

        #button
        self.btn_add.clicked.connect(self.addListWidget)
        self.btn_insert.clicked.connect(self.insertListWidget)

        self.btn_print.clicked.connect(self.printCurrentItem)
        self.btn_printMulti.clicked.connect(self.printMultiItems)
        self.btn_remove.clicked.connect(self.removeCurrentItem)
        self.btn_clear.clicked.connect(self.clearItem)


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
        insert_text = self.line_insertItem.text()
        selected_row = self.listWidget_Test.currentRow()

        if selected_row == -1:
            self.listWidget_Test.addItem(insert_text)
        else:
            self.listWidget_Test.insertItem(selected_row, insert_text)

    # Button
    def printCurrentItem(self) :
        print(self.listWidget_Test.currentItem().text())

    def printMultiItems(self) :
        self.selectedList = self.listWidget_Test.selectedItems()
        for i in self.selectedList :
            print(i.text())

    def removeCurrentItem(self):
        selected_items = self.listWidget_Test.selectedItems()
        rows = sorted([self.listWidget_Test.row(i) for i in selected_items], reverse=True)

        for row in rows:
            self.listWidget_Test.takeItem(row)


    def clearItem(self) :
        self.listWidget_Test.clear()


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass() 
    myWindow.show()
    app.exec()