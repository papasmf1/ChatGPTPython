챗GPT를 활용한 파이썬 프로그래밍

2023년 8월에 소스를 업데이트 한 이후에 변경이 생겨서 다시 업로드를 했습니다. 

네이버 블로그 크롤링 코드도 네이버 사이트가 업데이트되면서 아래 파일에 전체 수정된 코드를 추가했습니다. 
Chap09_ChatGPT로생성한네이버블로그검색231026.py

*pandasai에 관련된 코드가 많이 수정되었습니다. 
(버전 문제가 있기 때문에 기존 pandas는 제거하고 설치한다.) 

pip uninstall pandas 

pip install pandasAI

*pandasai와 관련된 내용은 아래의 사이트에서 해당 설명을 체크할 수 있습니다. 

https://github.com/gventuri/pandas-ai

*OpenAI에서 제공하는 키는 아래의 링크를 통해서 확인합니다. 

https://platform.openai.com/account/api-keys

*Streamlit에서 에러가 발생하면 아래와 같이 duckdb버전을 추가로 셋팅합니다. 
(IOException이 발생하는 경우 pandasAI가 사용하는 버전을 추가로 설치해야 합니다. 
아래와 같이 duckdb 버전을 명시해서 설치합니다. )
pip install duckdb==0.8.1
