
# QspinBox: 정수
# QDoubleSpinBox: 실수

# Value: SpinBox에서 값을 조절하지 않았을 때, 기본적으로 보여줄 값 지정

import sys
from PyQt6.QtWidgets import *
from PyQt6 import uic

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("2_10_SpinBox+DoubleSpinBox/spinbox.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        #spinBox
        self.spinBox_Test.valueChanged.connect(self.printValue) # spinBox 값이 변경되었을 때, 출력
        self.btn_showInfo.clicked.connect(self.printInfo) 
        self.btn_changeRangeStep.clicked.connect(self.changeRangeStep) # Change 버튼을 누르면 Range 설정값으로 변경

        #doubleSpinBox  
        self.doubleSpinBox_Test.valueChanged.connect(self.printDoubleValue)
        self.btn_doubleShowInfo.clicked.connect(self.printDoubleInfo)
        self.btn_doubleChangeRangeStep.clicked.connect(self.changeDoubleRangeStep)


    #spinBox
    def printValue(self) :   # 값이 변경되면 출력하는 기능
        print(self.spinBox_Test.value()) 
    
    def printInfo(self) :  # 클릭하면 아래 내용 출력
        print("Maximum value is", self.spinBox_Test.maximum()) # 기본 99
        print("Minimum value is", self.spinBox_Test.minimum()) # 기본 0
        print("Step Size is", self.spinBox_Test.singleStep())  # 기본 1
        # SingleStep: 버튼을 눌렀을 때 숫자가 얼마나 늘어나고 줄어드는지

    def changeRangeStep(self) :  # Range값 변경
        self.spinBox_Test.setRange(0,1000)
        self.spinBox_Test.setSingleStep(10) # 업다운 숫자 범위


    #doubleSpinBox
    def printDoubleValue(self) :
        print(self.doubleSpinBox_Test.value())

    def printDoubleInfo(self) :
        print("Maximum value is", self.doubleSpinBox_Test.maximum()) # 기본 99.99
        print("Minimum value is", self.doubleSpinBox_Test.minimum()) # 기본 0.0
        print("Step Size is", self.doubleSpinBox_Test.singleStep())  # 기본 1.0

    def changeDoubleRangeStep(self) :
        self.doubleSpinBox_Test.setRange(0,1000)
        self.doubleSpinBox_Test.setSingleStep(1.5)

        # 1000.0
        # 0.0
        # 1.5




if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass() 
    myWindow.show()
    app.exec()