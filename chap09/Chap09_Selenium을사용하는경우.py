#Chap09_Selenium을사용하는경우.py
# pip install clipboard 

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import clipboard
import time

driver = webdriver.Chrome()
driver.get('https://nid.naver.com/nidlogin.login')

# 로그인 창에 아이디/비밀번호 입력
loginID = "kim"
clipboard.copy(loginID)
#mac은 COMMAND, window는 CONTROL
driver.find_element(By.XPATH,'//*[@id="id"]').send_keys(Keys.CONTROL, 'v')

loginPW = "1234"
clipboard.copy(loginPW)
driver.find_element(By.XPATH,'//*[@id="pw"]').send_keys(Keys.CONTROL, 'v')
time.sleep(1)

# 로그인 버튼 클릭
driver.find_element(By.XPATH,'//*[@id="log.login"]').click()

while True:
    pass 