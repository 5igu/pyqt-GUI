import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6 import uic

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("2_17_ProgressBar/progressbar.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        #ProgressBar 시그널
        self.progressBar_Test.valueChanged.connect(self.printValue)

        # QTimer 설정
        self.timerVar = QTimer()               # QTimer 생성
        self.timerVar.setInterval(100)        # interval ms단위로 설정
        self.timerVar.timeout.connect(self.progressBarTimer) # interval마다 실행할 함수
        print("Timer Start!")
        self.timerVar.start()                  # 시간 체크 시작

        self.progressBar_Test.setValue(0)

        # self.progressBar_Test.setMaximum(80) 
        # 80으로 설정했을 때 : ui에서는 100%로 표기되지만, 실제 내부 값 범위는 80이 최대값임

    

    def progressBarTimer(self) :
        print("Count Start!")
        self.time = self.progressBar_Test.value()
        self.time += 1
        self.progressBar_Test.setValue(self.time)

        # progressBar가 최댓값 이상이면 중단
        if self.time >= self.progressBar_Test.maximum() :
            print("Timer Stop!")
            self.timerVar.stop()


    def printValue(self) :
        print(self.progressBar_Test.value())




if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass() 
    myWindow.show()
    app.exec()

    