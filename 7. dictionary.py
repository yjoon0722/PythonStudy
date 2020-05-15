# python의 dictionary = java의 map
# key: value 를 저장하는 list
lux = {'health': 490, 'mana': 334, 'melle': 550, 'armor': 18.72}

# 키가 중복되면 가장 뒤에 있는 값만 사용함.
lux = {'health': 490, 'health': 800, 'mana': 334, 'melee':550 ,'armor': 18.72}
lux['health']
lux # 중복되는 키는 저장되지 않음.

# dictionary의 value값은 문자열뿐만 아니라 정수, 실수, 불도 사용할 수 있으며 자료형을 섞어서 사용할 수 있다.
x = {100: 'hundred', False: 0, 3.5: [3.5, 3.5]}
# 단, key값에는 list와 dictionary를 사용할 수 없다.

# 빈 Dictionary 만들기
x = {}
y = dict()

# dict()를 이용한 dictionary 만들기
# 딕셔너리 = dict(key1=value1, key2=value2)
# 딕셔너리 = dict(zip([key1,key2],[value1,value2]))
# 딕셔너리 = dict([(key1,val1),(key2,val2)])
# 딕셔너리 = dict({key1:val1,key2,val2})

lux1 = dict(health=490, mana=334, melee=550, armor=18.72)
lux2 = dict(zip(['health','mana','melee','armor'],[490,334,550,18.72]))
lux3 = dict([('health',490),('mana',334),('melee',550),('armor',18.72)])
lux4 = dict({'health': 490, 'mana': 334, 'melle': 550, 'armor': 18.72})

# dictionary의 key에 value 할당하기
lux = {'health': 490, 'mana': 334, 'melle': 550, 'armor': 18.72}
lux['health']=2037
lux['mana']=1184
lux

# dictionary에 key가 있는지 확인하기
lux = {'health': 490, 'mana': 334, 'melle': 550, 'armor': 18.72}
'health' in lux # True
'attack_speed' in lux # False
# not in 도 사용가능
# leng()을 이용하여 key의 개수도 구할 수 있음

