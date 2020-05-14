# 값사이에 특정 문자넣기
print(1,2,3, sep=', ') # 1, 2, 3
print(4,5,6,sep=',') # 4,5,6
print('Hello','Python',sep='') # HelloPython
print(1920,1080,sep='x') # 1920x1080
print(1,2,3, sep='\n') # 1 줄바꿈 2 줄바꿈 3
print(1\n2\n3) # 위와동일

# print 함수의 end
print(1, end=''); print(2,end=''); print(3)
# end는 현재 print가 끝난 뒤 그다음에 오는 print 함수에 영향을 준다.
# end는 기본적으로 \n이 지정된 상태인데 빈 문자열을 지정하여 여러개의 print를 붙여쓸수 있다.

# 객체가 같은지 다른지 비교하기
1 == 1.0 # True
1 is 1.0 # False
1 is not 1.0 # True

# 객체가 다름을 확인하려면 id함수를 써서 객체 고유값을 구한다.
id(1) # 4316261024
id(1.0) # 4322178192

#값(숫자) 비교에는 is를 쓰지않는다
a = -5
a is -5
#True
a = -6
a is -6
#False
# 변수 a가 있는 상태에서 다른 값을 할당하면 메모리 주소가 달라질 수 있기 때문
# 따라서 다른 객체가 되므로 값이 같더라도 is로 비교하면 False가 출력

# 논리 연산자
True and True # True
True and False # False
False and True # False
False and False # False

True or True # True
True or False # True
False or True # True
False or False # False

not True # False
not False # True

# and, or, not 논리 연산자가 식 하나에 들어있으면 not, and, or 순으로 판단합니다.
not True and False or not False # True

# 정수 0, 실수 0.0이외의 모든 숫자는 True입니다. 그리고 빈 문자열 '', ""를 제외한 모든 문자열은 True입니다.
bool(1) # True
bool(0) # False
bool(1.5) # True
bool('False') # True
