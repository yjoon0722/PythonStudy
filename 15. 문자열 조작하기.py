# replace를 이용한 문자열 바꾸기
a = 'Hello, world!'
a.replace('world','Python')
print(a) # Hello, Python!

# maketrans를 이용한 문자 바꾸기
table = str.maketrans('aeiou','12345') # a를 1로 e를 2로 i를 3으로 o를 4로 u를 5로 바꾼다는 의미
print('apple'.translate(table))

# 구분자 문자열과 문자열 리스트 연결하기 (.split()으로 만들어진 문자열 리스트를 , 말고 다른걸로 연결하기)
a = 'apple pear grape pineapple orange'.split()
print(a) # ['apple', 'pear', 'grape', 'pineapple', 'orange']
a = ' '.join(a)
print(a) # apple pear grape pineapple orange
a = 'apple pear grape pineapple orange'.split()
a = '-'.join(a)
print(a) # apple-pear-grape-pineapple-orange

# 소문자를 대문자로 변경
a = 'python'; a = a.upper()
print(a)
# 대문자를 소문자로 변경
a = 'PYTHON'; a = a.lower()
print(a)

# 문자열의 공백 삭제하기
a = '   Python   '; a = a.lstrip() # 왼쪽에 있는 연속된 모든 공백 삭제
print(a) # 'Python   '
a = '   Python   '; a = a.rstrip() # 오른쪽에 있는 연속된 모든 공백 삭제
print(a) # '   Python'
a = '   Python   '; a = a.strip() # 양쪽에 있는 연속된 모든 공백 삭제
print(a) # 'Python'

# 문자열에서 특정 문자 삭제하기
a = ', python.'; a = a.lstrip(',.') # 왼쪽에서 ''안에 들어간 문자를 삭제
print(a) # ' python.' >> 공백은 넣지 않았으므로 공백은 유지
a = ', python.'; a = a.rstrip(',.') # 오른쪽에서 ''안에 들어간 문자를 삭제
print(a) # ', python'
a = ', python.'; a = a.strip(',.') # 양쪽에서 ''안에 들어간 문자를 삭제
print(a) # ' python'
