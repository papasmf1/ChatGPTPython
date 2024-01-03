#Chap07_random모듈.py
import random 

print("---랜덤하게 실수 생성---")
print(random.random())
print(random.random())
print("---구간을 2.0에서 5.0으로 지정---")
print(random.uniform(2,5))
print("---randrange()함수를 사용한 생성---")
print([random.randrange(20) for i in range(10)])
print([random.randrange(20) for i in range(10)])
print("---sample()함수를 사용한 생성---")
print(random.sample(range(20),10))
print(random.sample(range(20),10))

