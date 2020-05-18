import random

# while문 기본문장
i = 0
while i < 100:
    print('Hello, world!')
    i += 1 # Hello, world! 100번 출력

# 초기값을 감소시키기
i = 100
while i > 0:
    print('Hello, world!')
    i -= 1

# 입력한 횟수대로 반복하기
count = int(input('반복할 횟수를 입력하세요 : '))

i = 0 
while i < count: # i가 count보다 작을 때 반복
    print('Hello, world!', i)
    i += 1

while count > 0: # count가 0보다 클 때 반복
    print('Hello, world!', count)
    count -= 1

# python에서 난수를 생성하려면 random모듈이 필요함

x = random.random() # 랜덤한 실수 생성
print(x)

x = random.randint(1,6) # 랜덤한 정수를 생성하는 함수
print(x)

dice = [1,2,3,4,5,6]
x = random.choice(dice)
print('선택된숫자 :',x)

# random함수를 while문에 적용시키기
i = 0
while i != 3: # i가 3이 아니면 계속 반복
    i = random.randint(1,6)
    print(i)


