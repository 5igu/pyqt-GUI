import sys
from PyQt6.QtWidgets import *
from PyQt6 import uic

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("2_9_ComboBox/combobox.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        #test

        #프로그램 실행 시 두 개의 ComboBox를 동기화시키는 코드
        self.syncComboBox()

        #ComboBox에 기능 연결
        self.cmb_Test.currentIndexChanged.connect(self.comboBoxFunction)

        #버튼에 기능 연결
        self.btn_printItem.clicked.connect(self.printComboBoxItem)
        self.btn_clearItem.clicked.connect(self.clearComboBoxItem)
        self.btn_addItem.clicked.connect(self.addComboBoxItem)
        self.btn_deleteItem.clicked.connect(self.deleteComboBoxItem)


    def syncComboBox(self) :
        for i in range(0, self.cmb_Test.count()) :
            self.cmb_second.addItem(self.cmb_Test.itemText(i))

    def comboBoxFunction(self) :
        self.lbl_display.setText(self.cmb_Test.currentText())

    def clearComboBoxItem(self) :
        self.cmb_Test.clear()
        self.cmb_second.clear()

    def printComboBoxItem(self) :
        print(self.cmb_Test.currentText())

    def addComboBoxItem(self) :
        self.cmb_Test.addItem(self.lineEdit_Test.text())
        self.cmb_second.addItem(self.lineEdit_Test.text())
        print("Item Added")

    def deleteComboBoxItem(self) :
        self.delidx = self.cmb_second.currentIndex()
        self.cmb_Test.removeItem(self.delidx)
        self.cmb_second.removeItem(self.delidx)
        print("Item Deleted")



if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass() 
    myWindow.show()
    app.exec()