# 2차원 list는 java와 다를점이 없지만
# 2차원 tuple의 경우에는 살짝 특수하다.
a = ((10,20),(30,40),(50,60)) # tuple안에 tuple을 넣은 2차원 튜플
b = ([10,20],[30,40],[50,60]) # tuple안에 list를 넣음
c = [(10,20),(30,40),(50,60)] # list안에 tuple을 넣음

# a[0][0] = 500     # 안쪽 tuple은 변경할 수 없음. TypeError 발생
# a[0] = (500,600)  # 바깥쪽 tuple은 변경할 수 없음. TypeError 발생
b[0][0] = 500     # 안쪽 list는 변경할 수 있음.
# b[0] = (500,600)  # 바깥쪽 tuple은 변경할 수 없음. TypeError 발생
# c[0][0] = 500     # 안쪽 tuple은 변경할 수 없음.
c[0] = (500,600)  # 바깥쪽 list는 변경할 수 있음.

# 알아보기 쉽게 출력하기
from pprint import pprint
pprint(a, indent=4, width=20) # indent는 들여쓰기 칸 수 , width는 가로 폭입니다.

# for문을 한 번만 사용하기
a = [[10,20],[30,40],[50,60]]
for x,y in a: # in 앞의 변수의 갯수에 따라 안쪽 리스트에서 요소를 꺼내오는 갯수가 다르다.(변수가 2개면 요소 2개 변수가 3개면 요소 3개)
    print(x,y) # 10 20
               # 30 40
               # 50 60

# 이중 for문을 사용하기
a = [[10,20],[30,40],[50,60]]
for i in a:              # 안쪽 리스트를 통째로 꺼내고
    for j in i:          # 안쪽 리스트에서 요소를 하나하나 꺼낸다.
        print(j,end=' ')
    print()

# for와 range() 사용하기
a = [[10,20],[30,40],[50,60]]
for i in range(len(a)):          # 세로 크기 (안쪽 리스트의 개수)
    for j in range(len(a[i])):   # 가로 크기 (안쪽 리스트에 들어있는 요소의 개수)
        print(a[i][j], end=' ')  # 요소에 접근할 때는 list[][] 형식으로 접근한다.
    print()

# while문 이용
a = [[10,20],[30,40],[50,60]]

i = 0
while i < len(a):              # 세로 크기
    j = 0                      # i값이 증가할 때마다 j를0으로 초기화한다.(그래야 인덱스값이 초기화됨)
    while j < len(a[i]):       # 가로 크기
        print(a[i][j], end=' ')
        j += 1                 # 가로 인덱스를 1 증가시킴 // 안쪽에서 i를 증가시키면 안됨
    print()
    i += 1                     # 세로 인덱스를 1 증가시킴

# 반복문으로 1차원 list만들기
a = []
for i in range(10):
    a.append(0)
print(a) # [0,0,0,0,0,0,0,0,0,0,0]

# 반복문으로 2차원 list만들기
a = []
for i in range(3):        # 생성할 리스트 갯수
    line = []             # 안쪽 리스트로 사용할 빈 리스트 생성
    for j in range(2):    # 생성할 안쪽 리스트의 요소수
        line.append(0)    # 안쪽 리스트에 0 추가
    a.append(line)        # 전체 리스트에 안쪽 리스트를 추가
print(a) # [[0,0],[0,0],[0,0]]

# 위 식을 리스트 표현식으로 변형
a = [[0 for j in range(2)] for i in range(3)]
print(a) # [[0,0],[0,0],[0,0]]
# 좀 더 간결하게
a = [[0] * 2 for i in range(3)] # [0]에 2를 곱하면 [0,0]이 된다.
print(a) # [[0,0],[0,0],[0,0]]

# 가로 크기가 불규칙한 톱니형 리스트(jagged list) 만들기
a = [3,1,3,2,5]
b = []

for i in a:            # a의 요소를 하나씩 가져오고
    line = []
    for j in range(i): # 그 a의 요소만큼
        line.append(0) # 빈 list에 0을 넣는다
    b.append(line)     # 그걸 b에 넣는다

print(b) # [[0,0,0],[0],[0,0,0],[0,0],[0,0,0,0,0]]

# 위 식을 리스트 표현식으로 변형
a = [[0] * i for i in [3,1,3,2,5]]
print(a) # [[0,0,0],[0],[0,0,0],[0,0],[0,0,0,0,0]]

# sorted로 2차원 리스트 정렬하기
# sorted(반복가능한객체, key=정렬함수, reverse=True 또는 False)
students = [
    ['john','C',19],
    ['maria','A',25],
    ['andrew','B',7]
]
print(sorted(students,key=lambda student: student[1])) # 안쪽 리스트의 인덱스 1을 기준으로 정렬
print(sorted(students,key=lambda student: student[2])) # 안쪽 리스트의 인덱스 2를 기준으로 정렬

# 2차원 리스트(튜플)를 복사하는건 copy()가 아닌 copy.deepcopy()
a = [[10,20],[30,40]]
import copy
b = copy.deepcopy(a)
b[0][0] = 500
print(a) # [[10,20],[30,40]]
print(b) # [[500,20],[30,40]]

# 3차원 리스트
a = [[[0 for i in range(3)]for j in range(4)] for k in range(2)]
print(a) # [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]]
