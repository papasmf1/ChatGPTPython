#Chap09_DemoForm.py
#Chap09_DemoForm.ui(화면을 XML문서 저장) + Chap09_DemoForm.py(로직 코딩) 
import sys 
from PyQt5.QtWidgets import *
from PyQt5 import uic 

#디자인 문서를 로딩(파일명이 변경됨)
form_class = uic.loadUiType("Chap09_DemoForm2.ui")[0]

#윈도우 클래스 정의(QMainWindow로 변경)
class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    #슬롯메서드 추가 
    def firstClick(self):
        self.label.setText("첫번째 버튼 클릭")
    def secondClick(self):
        self.label.setText("두번째 버튼 클릭")
    def thirdClick(self):
        self.label.setText("세번째 버튼 클릭~~")

#모듈을 직접 실행했는지를 체크
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec_()
