#Chap10_DemoForm2.py 
#Chap10_DemoForm2.ui(화면을 XML문서 저장) + Chap10_DemoForm2.py(로직 코딩) 
import sys 
#Qt패키지를 임포트 
from PyQt5.QtWidgets import *
from PyQt5 import uic 
#웹사이트에 페이지 실행을 요청
import urllib.request
from bs4 import BeautifulSoup

#디자인 문서를 로딩
form_class = uic.loadUiType("c:\\work\\Chap10_DemoForm2.ui")[0]
#윈도우 클래스 정의(좀 더 기능이 많은 창 QMainWindow)
class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def firstClick(self):
        self.label.setText("첫번째 버튼")
    def secondClick(self):
        self.label.setText("두번째 버튼")
    def thirdClick(self):
        self.label.setText("세번째 버튼~~")

#모듈을 직접 실행했는지를 체크
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec_()
