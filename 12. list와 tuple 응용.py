# list에 요소 추가하기 append,extend,insert
a = [10,20,30]
a.append(500)
print(a) # [10,20,30,500]
len(a) # 4
# appned는 list끝에 요소 하나를 추가한다.
# method를 호출한 list가 변경되며 새 리스트가 생성되지 않음

# list안에 list를 추가하기
a = [10,20,30]
a.append([500,600])
print(a) # [10,20,30,[500,600]]
len(a) # 4
# [500,600]을 하나의 요소로 치기때문에 list의 길이는 4이다.

# list 확장하기
a = [10,20,30]
a.extend([500,600])
print(a) # [10,20,30,500,600]
len(a) # 5
# extend는 append를 여러번 사용해야 할때 사용한다.
# extend는 호출한 list와 다른 list를 연결하여 확장한다.

# list의 특정 index에 요소 추가하기
a = [10,20,30]
a.insert(2, 500)
print(a) # [10,20,500,300]
len(a) # 4

# insert는 append처럼 list안에 list를 넣을 수 있다.
a = [10,20,30]
a.insert(1,[500,600])
print(a) # [10,[500,600],20,30]

# list 중간에 여러개의 요소를 추가할 경우 슬라이스를 사용하면된다.
a = [10,20,30]
a[1:1] = [500,600]
print(a) # [10,500,600,20,30]

# list에서 요소 삭제하기 pop,remove
a = [10,20,30]
a.pop()
print(a) # [10,20]

# 특정 인덱스 제거하기
a = [10,20,30]
a.pop(1)
print(a) # [10,30]

# pop대신에 del을 사용해도 된다.
a = [10,20,30]
del a[1]
print(a) # [10,30]

# 특정 값 삭제하기
a = [10,20,30]
a.remove(20)
print(a) # [10,30]

# 중복값이 있는경우 가장 앞쪽의 index에 있는 값을 지운다.
a = [10,20,30,20]
a.remove(20)
print(a) # [10,30,20]

# list로 queue 만들기
from collections import deque # deque : 반복 가능한 객체

a = deque([10,20,30])
a.append(500) # 덱의 오른쪽에 500 추가
print(a) # deque([10,20,30,500])
a.popleft() # 덱의 왼쪽 요소 하나 삭제
print(a) # deque([20,30,500])

# queue란? 리스트의 값을 선입 선출 할 수 있는 구조
# insert(값)를 하면 리스트의 맨뒤에 삽입 pop()을 하면 리스트의 맨앞에서 삭제를 하는 구조이다.

# list에서 특정 값의 인덱스 구하기
a = [10,20,30,15,20,40]
a.index(20) # 1
# 중복된 값이 있는경우 가장 앞의(가장 처음으로 찾은) index번호를 출력해준다

# 특정 값의 개수 구하기
a = [10,20,30,15,20,40]
a.count(20) # 2

# list의 순서 뒤집기
a = [10,20,30,15,20,40]
a.reverse()
print(a) # [40,20,15,30,20,10]

# list의 요소를 정렬하기
a = [10,20,30,15,20,40]
a.sort() # 혹은 a.sort(reverse=False) >> 오름차순 정렬
print(a) # [10,15,20,20,30,40]
a.sort(reverse=True) # 내림차순 정렬
print(a) # [40,30,20,20,15,10]

# sort()와 sorted()의 차이
a = [10,20,30,15,20,40]
a.sort() # a의 내용을 변경하여 정렬
print(a)
b = [10,20,30,15,20,40]
sorted(b) # 정렬된 새 리스트를 생성
print(b)

# list의 모든 요소 삭제하기
a = [10,20,30]
a.clear() # clear() 대신에 del a[:]로도 사용이 가능하다.
print(a) # []

# list를 슬라이스로 조작하기
a = [10,20,30]
a[len(a):] = [500] # == a.append(500)
print(a) # [10,20,30,500]

a = [10,20,30]
a[len(a):] = [500,600] # == a.extend([500,600])
print(a) # [10,20,30,500,600]

# list의 할당과 복사
a = [0,0,0,0,0]
b = a
# b = a와 같이 리스트를 다른 변수에 할당하면 리스트는 두 개가 될 것 같지만 실제로는 리스트가 한 개이다.
print(a is b) # True

# a와 b는 같으므로 리스트 b의 요소를 변경하면 리스트a 와 b에 모두 반영된다.
b[2] = 99
print(a) # [0,0,99,0,0]
print(b) # [0,0,99,0,0]

# 리스트 a와 b를 완전히 두 개로 만들려면 copy 메서드를 사용해야한다.
a = [0,0,0,0,0]
b = a.copy()
print(a is b) # False
print(a == b) # True

# 이제 a와 b는 별개이므로 한쪽값을 변경해도 다른 리스트에 영향을 미치지 않는다.
b[2] = 99
print(a) # [0,0,0,0,0]
print(b) # [0,0,99,0,0]

# for문을 이용한 list요소 출력하기
a = [38,21,53,62,19]
for i in a:
    print(i) # 38 \n 21 \n 53 \n 62 \n 19

# index번호와 요소를 함께 출력하기
a = [38,21,53,62,19]
for index, value in enumerate(a):
    print(index, value)
# 0 38
# 1 21
# 2 53
# 3 62
# 4 19

# index번호 0번을 1번으로 하여 출력하고 싶을 때
for index, value in enumerate(a):
    print(index + 1, value)
# 좀 더 파이썬 다운 방법
for index, value in enumerate(a,start=1): # eunumerate(a,1) 로 줄여서 사용도 가능함
    print(index, value)

# while문을 이용한 요소 출력하기
a = [38,21,53,62,19]
i = 0
while i < len(a):
    print(a[i])
    i += 1

# list에서 가장 작은 수와 큰 수 구하기
a = [38,21,53,62,19]
samllest = a[0] # list의 임의의 값을 변수에 저장하고
for i in a: 
    if i < samllest: # 모든 요소를 변수의 값과 비교를 해서
        samllest = i # 새로받은 요소가 변수의 값보다 작다면 변수에 저장
print(samllest) # 19
largest = a[0]
for i in a:
    if i > largest: # 크다면 저장
        largest = i
print(largest) # 62

# 요소의 합 구하기
a = [10,20,30,40,50]
x = 0
for i in a:
    x += i
print(x) # 150
# 귀찮기 때문에 python에서는 sum()함수를 제공한다.
x = sum(a)
print(x) # 150

# list 표현식 사용하기
# python에서는 list안에 for문과 if문을 사용할 수 있다.
# list에 for문 사용하기
a = [i for i in range(10)] # 숫자 10개 생성을 하고 숫자를 하나씩 꺼내어 i로 리스트를 생성함.
print(a) # [1,2,3,4,5,6,7,8,9]
b = list(i for i in range(10))
print(b) # [1,2,3,4,5,6,7,8,9]

# i를 다른값과 연산시키면 각 연산의 결과를 리스트로 생성합니다.
c = [i + 5 for i in range(10)]
print(c) # [5,6,7,8,9,10,11,12,13,14]
d = [i * 2 for i in range(10)]
print(d) # [0,2,4,6,8,10,12,16,18]

# list에 for문과 if문 사용하기
a = [i for i in range(10) if i % 2 == 0] # 숫자 10개를 생성하고 짝수만 뽑아내어 i로 리스트를 생성함.
print(a) # [0,2,4,6,8]

# list에 이중 for문을 사용하기
a = [i * j for j in range(2,10)  # 들여쓰기를 해도 되고 안해도 되지만 가독성을 위해선 들여쓰기로 맞춰주자
           for i in range(1,10)] # 처리순서는 뒤쪽에있는 문장부터 처리된다.
print(a) # 2단부터 9단 까지의 구구단이 출력됨 [2,4,6,8,...,63,72,81]

# list에 map사용하기
a = [1.2,2.5,3.7,4.6]
a = list(map(int,a))
print(a) # [1,2,3,4]

a = list(map(str,range(10)))
print(a) # ['0','1','2','3','4','5','6','7','8','9']

# list의 표현식와 tuple의 표현식은 대부분 같다.
# 대신 for문이나 if문을 사용하며 tuple을 생성 할 때는 예외가 있다.
# a = (i for i in range(10) if i % 2 == 0)
# print(a) # tuple이 아닌 generator 표현식으로 생성됨.
# 올바른 방법
a = tuple(i for i in range(10) if i % 2 == 0)
print(a) # (0,2,4,6,8)
