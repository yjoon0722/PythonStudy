# 문자열을 묶는 방법
hello = 'Hello, world!'
hello2 = "Hello, world!"
hello3 = '''Hello, world!'''
hello4 = """Hello, world!"""

#여러 줄로 된 문자열 사용하기
hello5 = '''Hello, world!
안녕하세요.
Python입니다. '''
print(hello5) # Hello,world!
              # 안녕하세요
              # Python입니다.
# 큰따옴표로도 가능함

# 문자열안에 작은따옴표나 큰따옴표 포함하기
s = "Python isn't difficult"
s1 = 'He said "Python is easy"'
# 작은따옴표안에 작은따옴표나 큰따옴표안에 큰따옴표는 사용할 수 없다.

# 예외적으로 ''' 나 """로 묶은 문자열은 동일따옴표 중복사용이 가능하다.
single_quote = '''"안녕하세요"
'파이썬'입니다'''
double_quote = """"Hello"
'Python'"""
double_quote2 = """Hello, 'Python'"""

# '''나 """를 사용하지않고 문자열에 동일따옴표 넣는방법
'Python isn\'t difficult' # "Python isn't difficult"

