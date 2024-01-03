import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

search_keyword='맥북에어'

url = f'https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search_keyword}'

response = requests.get(url)

#<a href="https://blog.naver.com/pareko" class="sub_txt sub_name" target="_blank" onclick="return goOtherCR(this, 'a=rvw*b.writer&amp;r=2&amp;i=90000003_0000000000000033ECA5C9EE&amp;u='+urlencode(this.href))">순돌아범</a>

soup = BeautifulSoup(response.text, 'html.parser')

# create a new Excel workbook and select the active sheet\
wb = Workbook()
ws = wb.active

# write the column names to the first row of the sheet
ws.append(["블로그명", "블로그주소", "글 제목", "포스팅 날짜"])

for page in range(1, 101):
    url = f'https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search_keyword}&start={page * 10 - 9}'

    posts = soup.find_all('li', {'class':'bx'})
    for post in posts:
        #<div class="user_info"> <a href="https://blog.naver.com/oksk2002kr" class="name" target="_blank" onclick="return goOtherCR(this, 'a=rvw*w.writer&amp;r=7&amp;i=90000003_0000000000000033F9F506CE&amp;u='+urlencode(this.href))">티보의 IT 리뷰 공작소</a> <div class="etc">인플루언서</div> <span class="sub">2주 전</span> </div>
        try:
            blog_address_elem = post.find("a", 
                attrs={"class":"name"}) 
            blog_address = blog_address_elem["href"]
            blog_address_title_elem = post.find("a", 
                            attrs={"class":"name"}) 
            blog_address_title = blog_address_title_elem.text 
        except TypeError:
            blog_address = "" 
            blog_address_title = ""
        

        post_date_elem = post.find('span', {'class':'sub'})
        post_date = post_date_elem.text if post_date_elem else ""
        post_title_elem = post.find('a',
            {'class':'title_link _cross_trigger'})
        post_title = post_title_elem.text if post_title_elem else "" 

        print(blog_address)
        print(blog_address_title)
        print(post_title)
        print(post_date)

        ws.append([blog_address, blog_address_title, post_title, post_date])

path = 'c:\\work\\'
file_path = f'{path}{search_keyword}_blog_data.xlsx'
wb.save(file_path)
