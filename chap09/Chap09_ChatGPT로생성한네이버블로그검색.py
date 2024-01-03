#Chap09_ChatGPT로생성한네이버블로그검색.py
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

search_keyword='맥북에어'

url = f'https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search_keyword}'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

wb = Workbook()
ws = wb.active

ws.append(["블로그명","글 제목", "포스팅 날짜"])

for page in range(1, 101):
    url = f'https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search_keyword}&start={page * 10 - 9}'
    print(url)
    posts = soup.find_all('li', {'class':'bx _svp_item'})
    for post in posts:
        blog_name = post.find('a', {'class':'sub_txt sub_name'}).text
        try:
            blog_address = blog_name['href']
        except TypeError:
            blog_address = "" 

        post_date_elem = post.find('span', {'class':'sub_time sub_txt'})
        post_date = post_date_elem.text if post_date_elem else ""
        post_title_elem = post.find('a',
            {'class':'api_txt_lines total_tit _cross_trigger'})
        post_title = post_title_elem.text if post_title_elem else "" 

        print(blog_name)
        print(blog_address)
        print(post_title)
        print(post_date)

        ws.append([blog_name, blog_address, post_title, post_date])

path = 'c:\\work\\'
file_path = f'{path}{search_keyword}_blog_data.xlsx'
wb.save(file_path)
