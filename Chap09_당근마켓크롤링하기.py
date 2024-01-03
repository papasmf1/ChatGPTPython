#Chap09_당근마켓크롤링하기.py
import urllib.request
from bs4 import BeautifulSoup

url = "https://www.daangn.com/hot_articles"
page = urllib.request.urlopen(url).read() 

soup = BeautifulSoup(page, 'html.parser')

posts = soup.find_all("div", attrs={"class":"card-desc"})
for post in posts:
   title = post.find("h2", attrs={"class":"card-title"})
   price = post.find("div", attrs={"class":"card-price"})
   addr = post.find("div", attrs={"class":"card-region-name"})
   print("{0} , {1} , {2}".format(title.text, price.text, addr.text))

#선택한 영역을 주석처리하기: ctrl + / 
# <div class="card-desc">
#       <h2 class="card-title">픽시</h2>
#       <div class="card-price ">
#         30,000원
#       </div>
#       <div class="card-region-name">
#         인천 계양구 작전동
#       </div>

