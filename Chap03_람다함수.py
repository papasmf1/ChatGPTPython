#Chap03_람다함수.py

#람다 함수 정의
g = lambda x,y:x*y
print( g(2,3) )
print( g(3,5) )
print( (lambda  x:x*x)(3) )
print( globals() )