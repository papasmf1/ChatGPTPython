#Chap09_클리앙중고장터검색_키워드검색.py
# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

#수집한 결과를 파일에 저장
f = open("clien.txt", "wt", encoding="utf-8")
for n in range(0,10):
        #클리앙의 중고장터 주소 
        url ='https://www.clien.net/service/board/sold?&od=T31&po=' + str(n)
        print(url)
        data = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(data, 'html.parser')
        list = soup.find_all('span', 
            attrs={'data-role':'list-title-text'})
        # <span class="subject_fixed" data-role="list-title-text">
		# 		맥북프로 M2 13인치 24/512 실버
		# </span>
        for item in list:
            title = item.text.strip()  
            if re.search("아이폰", title):
                print(title)
                f.write(title + "\n")

f.close() 

        
