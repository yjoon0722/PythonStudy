# 표준 입력으로 2차원 리스트의 가로(col)와 세로(row)가 입력되고 그 다음 줄부터 리스트의 요소로 들어갈 문자가 입력됩니다. 
# 이때 2차원 리스트 안에서 *는 지뢰이고 .은 지뢰가 아닙니다.
# 지뢰가 아닌 요소에는 인접한 지뢰의 개수를 출력하는 프로그램을 만드세요(input에서 안내 문자열은 출력하지 않아야 합니다).

# 여러 줄을 입력 받으려면 다음과 같이 for 반복문에서 input을 호출한 뒤
# append로 각 줄을 추가하면 됩니다(list 안에 문자열을 넣으면 문자열이 문자 리스트로 변환됩니다).
# matrix = []
# for i in range(row):
#     matrix.append(list(input()))

# 이 문제는 지금까지 심사문제 중에서 가장 어렵습니다.
# 처음 풀어보는 경우 대략 두 시간은 걸립니다. 시간을 두고 천천히 고민해서 풀어보세요.
# 지금까지 학습한 내용을 모두 동원해야 풀 수 있으며 막힐 때는 지금까지 학습한 내용을 다시 복습하면서 힌트를 찾아보세요.

col,row = map(int,input().split()) # 지뢰판의 넓이를 받고
matrix = [] # 지뢰를 넣을 빈 리스트를 생성한다음에
for i in range(row):
    matrix.append(list(input())) # 빈 리스트에 각각의 행에 지뢰를 넣어주고
for x in range(row):
    for y in range(col):
        if matrix[x][y] == '*': # 특정 인덱스의 값이 지뢰라면
            print(matrix[x][y],sep='',end='') # 지뢰를 그대로 출력하고
        else: # 지뢰값이 아니라면
            count = 0 # 주변에 지뢰가 몇개있는지를 담을 변수를 하나 선언
            for xo in range(-1,2): # 본인기준의 인덱스에서 -1~+1까지를 비교해야하니 range()를 이용
                for yo in range(-1,2):
                    if 0 <= x+xo < row and 0 <= y+yo < col and matrix[x+xo][y+yo] == '*': # 본인인덱스에서 -1~+1 까지를 해준값을 비교를 하는데
                        count += 1                                                         # 그 범위는 만들어놓은 인덱스 번호들의 범위를 넘을수 없고
            print(count,sep='',end='')                                                     # 범위를 넘지 않는곳에 지뢰가있다면 지뢰의갯수를 담는다.
    print() # 그리고 그걸 출력한다.
# 본인 [col][row]에서 [col-1][row-1]~[col+1][row+1]까지 를 비교
#
