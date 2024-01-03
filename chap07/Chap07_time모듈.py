#Chap07_time모듈.py
import time 

print(time.time())
time.sleep(5)
print(time.time())

print("---표준시간---")
print(time.gmtime())
print("---한국시간---")
print(time.localtime())
