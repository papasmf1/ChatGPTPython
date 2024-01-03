#Chap03_이름해석규칙.py

#전역변수 
x = 10 
y = 20 

#함수 정의
def func():
    return x+y 

#호출
print( func() )

#함수 정의
def func2():
    x = 1
    return x+y 

#호출
print( func2() )

