# 여러 개의 변수를 한번에 만들기
x, y, z = 10, 20, 30 # x=10 y=20 z=30
x = y = z = 10 # x=10 y=10 z=10

# 두 변수의 값 변경하기
x,y = 10, 20
x,y = y, x # x=20 y=10

# 변수 삭제하기
x = 10
del x

# 빈 변수 만들기
x = None # 다른언어의 null값은 파이썬에선 None이다.

# 입력 값을 변수에 저장하기
x = input()
# Hello, world!
print(x) # 'Hello, world!'
type(x) # <class 'str'>
# input 함수로 값을 입력받으면 str타입으로 저장이된다.
a=input('first number'); b=input('second number')
10
20
print(a+b) #1020 # a='10',b='20'
# 입력된 값을 정수로 바꾸려면 input 함수를 int로 감싸면된다

# 한번의 input 함수로 여러개의 변수에 저장하기
a,b,c = input('문자열').split('기준문자열')
# z zz zzz # a='z' b='zz' c='zzz'

# map을 이용한 정수변환
a, b = map(int,input().split())
10
20
print(a+b) # 30

