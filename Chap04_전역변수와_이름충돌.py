#Chap04_전역변수와이름충돌 
#전역변수
strName = "전역변수의 값"
class DemoString:
    def __init__(self):
        self.strName = "" 
    def set(self, msg):
        self.strName = msg
    def print(self):
        #이부분을 수정했습니다. 
        print(self.strName)

g = DemoString()
g.set("멤버변수에 셋팅")
g.print()

