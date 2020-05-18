import turtle as t

# 네모그리기
t.shape('turtle')
t.forward(100)
t.right(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.mainloop()

# 반복문을 사용한 다각형 그리기
t.shape('turtle')
for i in range(4):    # 사각형이므로 4번 반복
    t.forward(100)
    t.right(90)
    t.mainloop()

t.shape('turtle')
for i in range(5):      # 오각형이므로 5번 반복
    t.forward(100)
    t.right(360 / 5)    # 360을 5로 나누어서 외각을 구함
    t.mainloop()

n = int(input())        # 사용자의 입력을 받음
t.shape('turtle')
for i in range(n):      # n번 반복
    t.forward(100)
    t.right(360 / n)    # 360을 n으로 나누어서 외각을 구함
    t.mainloop()

# 다각형에 색칠하기
n = 6    # 육각형
t.shape('turtle')
t.color('red')          # 펜의 색을 빨간색으로 설정
t.begin_fill()          # 색칠할 영역 시작
for i in range(n):      # n번 반복
    t.forward(100)
    t.right(360 / n)    # 360을 n으로 나누어서 외각을 구함
t.end_fill()            # 색칠할 영역 끝
t.mainloop()
# 색영역에는 css에 사용하는 웹색상도 사용가능.

# 원그리기
t.shape('turtle')
t.circle(120) # 반지름이 120인 원 그리기

# 여러번 그리기
n = 60    # 원을 60번 그림
t.shape('turtle')
t.speed('fastest')      # 거북이 속도를 가장 빠르게 설정
for i in range(n):
    t.circle(120)       # 반지름이 120인 원을 그림
    t.right(360 / n)    # 오른쪽으로 6도 회전

# 복잡한 무늬 그리기
t.shape('turtle')
t.speed('fastest')      # 거북이 속도를 가장 빠르게 설정
for i in range(300):    # 300번 반복
    t.forward(i)        # i만큼 앞으로 이동. 반복할 때마다 선이 길어짐
    t.right(91)         # 오른쪽으로 91도 회전

# 터틀 모양 설정하기 및 현재 모양 알아내기
t.shape('arrow')    # 화살표 모양 사용 'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic' 등이 있음
t.shape()           # 현재 모양 알아내기