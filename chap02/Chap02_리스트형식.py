#Chap02_리스트형식.py
lst = [1,2,3,4,5]
print( type(lst) )
print( len(lst) )
print( lst )

#리스트에 입력, 수정, 삭제하기 
lst.append(6)
lst.insert(1,20)
lst[0] = 100 
lst.remove(5)
print( lst )