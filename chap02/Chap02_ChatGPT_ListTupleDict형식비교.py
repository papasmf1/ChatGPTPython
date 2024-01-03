#Chap02_ChatGPT_ListTupleDict형식비교.py
# List
my_list = [1, 2, 3, 4, 5]

# Tuple
my_tuple = (1, 2, 3, 4, 5)

# Dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# List 장점: 요소 추가 및 삭제가 용이하다.
my_list.append(6)
my_list.remove(3)
print("List:", my_list)

# Tuple 단점: 요소 추가 및 삭제가 불가능하다.
# my_tuple.append(6)  # 에러 발생
# my_tuple.remove(3)  # 에러 발생
print("Tuple:", my_tuple)

# Dict 장점: 키-값 쌍으로 데이터를 저장하므로 데이터 접근이 용이하다.
print("Dictionary value with key 'c':", my_dict['c'])

# List, Tuple 단점: 요소에 접근할 때 인덱스를 사용해야 한다.
print("Accessing List element by index:", my_list[2])
print("Accessing Tuple element by index:", my_tuple[2])

# Dict 단점: 순서가 보장되지 않으므로 인덱스를 사용할 수 없다.
# print("Accessing Dictionary element by index:", my_dict[2])  # 에러 발생

# List, Tuple 장점: 여러 타입의 요소를 포함할 수 있다.
mixed_list = [1, 'a', True, 3.14]
mixed_tuple = (1, 'a', True, 3.14)
print("Mixed List:", mixed_list)
print("Mixed Tuple:", mixed_tuple)

# Dict 장점: 유연한 데이터 구조로 키와 값을 연결할 수 있다.
student = {'name': 'John', 'age': 20, 'major': 'Computer Science'}
print("Student Name:", student['name'])
print("Student Age:", student['age'])
print("Student Major:", student['major'])
