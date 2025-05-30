import sys
from PyQt6.QtWidgets import *
from PyQt6 import uic

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("2_11_Slider+Dial/sliderDial.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        #vertical
        self.verticalSlider_Test.valueChanged.connect(self.showVerticalSliderValue)
        self.verticalSlider_Test.rangeChanged.connect(self.printRangedChanged)
        
        #horizontal
        self.horizontalSlider_Test.valueChanged.connect(self.showHorizontalSliderValue)
        self.horizontalSlider_Test.rangeChanged.connect(self.printRangedChanged)

        #dial
        self.dial_Test.valueChanged.connect(self.showDialValue)
        self.dial_Test.rangeChanged.connect(self.printRangedChanged)

        #button
        self.btn_VInfo.clicked.connect(self.getVerticalInfo)
        self.btn_VRange.clicked.connect(self.setVertical)
        
        self.btn_HInfo.clicked.connect(self.getHorizontalInfo)
        self.btn_HRange.clicked.connect(self.setHorizontal)

        self.btn_DInfo.clicked.connect(self.getDialInfo)
        self.btn_DRange.clicked.connect(self.setDial)


    def printRangedChanged(self) :
        print("Range Changed")

    # Vertical
    def showVerticalSliderValue(self) :
        self.labelVertical.setText(str(self.verticalSlider_Test.value()))

    def getVerticalInfo(self) :
        print("Maximum: " + str(self.verticalSlider_Test.maximum()))          # 99
        print("Minimum: " + str(self.verticalSlider_Test.minimum()))          # 0
        print("PageStep: " + str(self.verticalSlider_Test.pageStep()))        # 10
        print("SingleStep: " + str(self.verticalSlider_Test.singleStep()))    # 1

    def setVertical(self) :
        # self.verticalSlider_Test.setMaximum(500)
        # self.verticalSlider_Test.setMinimum(-500)
        # printRangedChanged에서 "Range Changed"가 두 번 출력되어서 Range로 한 번만 출력되도록 변경

        self.verticalSlider_Test.setRange(-500, 500) 
        self.verticalSlider_Test.setPageStep(100)  # Page Up/Down으로 이동할 수 있는 값
        self.verticalSlider_Test.setSingleStep(20)  # Slider 조작이나 방향키로 이동할 수 있는 값


    # Horizontal
    def showHorizontalSliderValue(self) :
        self.labelHorizontal.setText(str(self.horizontalSlider_Test.value()))

    def getHorizontalInfo(self) :
        print("Maximum: " + str(self.horizontalSlider_Test.maximum()))
        print("Minimum: " + str(self.horizontalSlider_Test.minimum()))
        print("PageStep: " + str(self.horizontalSlider_Test.pageStep()))
        print("SingleStep: " + str(self.horizontalSlider_Test.singleStep()))

    def setHorizontal(self) :
        self.horizontalSlider_Test.setRange(-500, 500)
        self.horizontalSlider_Test.setPageStep(100)  # Page Up/Down으로 이동할 수 있는 값
        self.horizontalSlider_Test.setSingleStep(20)  # Slider 조작이나 방향키로 이동할 수 있는 값


    # Dial
    def showDialValue(self) :
        self.labelDial.setText(str(self.dial_Test.value()))

    def getDialInfo(self) :
        print("Maximum: " + str(self.dial_Test.maximum()))        # 99
        print("Minimum: " + str(self.dial_Test.minimum()))        # 0
        print("PageStep: " + str(self.dial_Test.pageStep()))      # 10
        print("SingleStep: " + str(self.dial_Test.singleStep()))  # 1

    def setDial(self) :
        self.dial_Test.setRange(-500, 500)
        self.dial_Test.setPageStep(100)
        self.dial_Test.setSingleStep(20)

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass() 
    myWindow.show()
    app.exec()