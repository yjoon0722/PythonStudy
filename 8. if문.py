# if문 기본문장
x=10
if x == 10:
    print('10입니다.')

# if문 다음줄에 아무 코드도 넣지 않으면 에러가 발생하므로 pass를 넣어야한다.
if x == 10:
    pass

# 들여쓰기에 따라 if문안에 들어갈지 들어가지 않을지가 결정된다.
x = 5
if x == 10:
    print('x에 들어있는 숫자는') # if문의 조건에 일치하지 않음 
print('10입니다.') # 위의 if문과는 상관없는 코드

# if,else문 기본문장
x = 5
if x == 10:
    y = x
else:
    y = 0

# 변수에 값을 할당하는 if,else문 축약
x = 5
y = x if x == 10 else 0

# 조건식이 아닌 값의 if,else문
if True:
    print('참') # True는 참
else:
    print('거짓')
if False:
    print('참')
else:
    print('거짓') # False는 거짓
if None:
    print('참')
else:
    print('거짓') # None은 거짓
# None은 False로 취급되므로 else의 코드가 실행된다.
# 실제 코드를 작성할 때 변수에 들어있는 값이나 함수의 결과가 None인 경우가 많다

# if 조건문에 숫자 지정하기
# 숫자는 정수(2진수, 10진수, 16진수), 실수와 관계없이 0이면 거짓, 0이 아닌 수는 참입니다.
if 0:
    print('참')
else:
    print('거짓')    # 0은 거짓
 
if 1:
    print('참')    # 1은 참
else:
    print('거짓')
 
if 0x1F:    # 16진수
    print('참')    # 0x1F는 참
else:
    print('거짓')
 
if 0b1000:    # 2진수
    print('참')    # 0b1000은 참
else:
    print('거짓')
 
if 13.5:    # 실수
    print('참')    # 13.5는 참
else:
    print('거짓')

# if 조건문에 문자열 지정하기
if 'Hello':    # 문자열
    print('참')    # 문자열은 참
else:
    print('거짓')
 
if '':    # 빈 문자열
    print('참')
else:
    print('거짓')    # 빈 문자열은 거짓

# 그외에 True,False로 취급하는 것들
# 다음은 파이썬 문법 중에서 False로 취급하는 것들입니다.
# None
# False
# 0인 숫자들: 0, 0.0, 0j
# 비어 있는 문자열, 리스트, 튜플, 딕셔너리, 세트: '', "", [], (), {}, set()
# 클래스 인스턴스의 __bool__(), __len__() 메서드가 0 또는 False를 반환할 때
# 앞에서 나열한 것들을 제외한 모든 요소들은 True로 취급합니다.