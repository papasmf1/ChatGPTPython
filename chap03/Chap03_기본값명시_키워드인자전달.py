#Chap03_기본값명시_키워드인자전달.py
#함수 정의 
def times(a=10, b=20):
    return a*b 

#호출 
print( times() )
print( times(5) )
print( times(5,6) )

#키워드인자전달(파라메터명을 명시)
def connectURI(server, port):
    strURL = "http://" + server + ":" + port 
    return strURL

#호출 
print( connectURI("naver.com", "80") )
print( connectURI(port="8080", server="naver.com") )