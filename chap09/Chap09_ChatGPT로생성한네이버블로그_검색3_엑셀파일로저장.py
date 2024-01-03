#Chap09_ChatGPT로생성한네이버블로그검색3_엑셀파일로저장.py 
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

def crawl_naver_blog(search_keyword):
    # Create a new workbook
    wb = Workbook()
    # Get the active sheet
    sheet = wb.active
    # Set the column headers
    sheet.append(["Blog Name", "Blog Address", "Post Title", "Posting Date"])
    
    # Iterate through page numbers from 1 to 100
    for page in range(1, 101):
        # Format the URL with the search keyword and page number
        url = f"https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search_keyword}&start={page*10-9}"
        
        # Send a GET request to the URL
        response = requests.get(url)
        
        # Create a BeautifulSoup object with the response content
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Find the relevant tags that contain the blog information
        blog_tags = soup.find_all("li", class_="bx _svp_item")
        
        # Check if no more results found
        if not blog_tags:
            print("No more results found.")
            break
        
        # Iterate over the blog tags and extract the required information
        for post in blog_tags:
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
            
            # Print the extracted information
            print("Blog Name:", blog_name)
            print("Blog Address:", blog_address)
            print("Post Title:", post_title)
            print("Posting Date:", post_date_elem)
            print()

            # Append the extracted information to the sheet
            sheet.append([blog_name, blog_address, post_title, post_date])
    
    # Save the workbook as an Excel file
    wb.save("c:\\work\\search_results.xlsx")
    print("Excel file saved successfully.")

# Call the function with the search keyword
crawl_naver_blog("맥북에어")
