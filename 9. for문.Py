# for와 range 사용하기
for i in range(100):
    print('Hello, world!') # Hello, world! 가 100번 출력되는 코드

# range()문이기 때문에 증가폭과 감소폭이 사용 가능하다.
for i in range(5, 12):    # 5부터 11까지 반복
    print('Hello, world!', i)
for i in range(0, 10, 2):    # 0부터 8까지 2씩 증가
    print('Hello, world!', i)
for i in range(10, 0, -1):    # 10에서 1까지 1씩 감소
    print('Hello, world!', i)
# 증가폭을 음수로 지정하는 방법말고 reversed를 사용하면 숫자의 순서를 반대로 뒤집을 수 있다.
for i in reversed(range(10)):    # range에 reversed를 사용하여 숫자의 순서를 반대로 뒤집음
    print('Hello, world!', i)    # 9부터 0까지 10번 반복

# 입력한 횟수대로 반복하기
count = int(input('반복할 횟수를 입력하세요.'))

for i in range(count):
    print('Hello, world!',i)

# range대신 시퀀스 객체로 반복하는 for문
a = [10,20,30,40,50]
for i in a:
    print(i)

fruits = ('apple','orange','grape')
for fruit in fruits:
    print(fruit)

for letter in 'Python':
    print(letter,end=' ')