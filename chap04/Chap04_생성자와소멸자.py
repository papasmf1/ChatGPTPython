#Chap04_생성자와소멸자.py 
class DemoClass:
    #생성자(인스턴스를 생성할 때 가장 먼저 실행)
    def __init__(self, value):
        self.value = value
        print("인스턴스가 생성되었습니다. value:", value)
    #소멸자(인스턴스를 소멸할 때 가장 마지막에 실행)
    def __del__(self):
        print("인스턴스가 소멸되었습니다.")

#인스턴스 생성
d = DemoClass(5)
del d 

print("전체 코드 실행 종료")
