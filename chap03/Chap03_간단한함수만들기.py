#Chap03_간단한함수만들기.py
#함수정의
def setValue(newValue):
    #지역변수
    x = newValue
    print("지역변수 x:", x)

#호출
retValue = setValue(5)
print(retValue)

#함수정의
def swap(x,y):
    return y,x 

#호출
print( swap(3,4) )
