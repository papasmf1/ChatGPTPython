#Chap07_datetime모듈.py
from datetime import * 

d1 = date(2023, 6, 1) 
print( d1 )
print("---오늘날짜를 리턴---")
d2 = date.today() 
print( d2 )
print("100일을 더하면:{0}".format(d2))
d3 = timedelta(days=100)
print( d2 + d3 )
d4 = datetime.now()
print("현재 날짜와 시간을 출력:{0}".format(d4))
