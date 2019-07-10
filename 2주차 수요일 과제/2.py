name=input('캐릭터의 이름을 입력하세요: ')

print(f'캐릭터 이름: {name}')
import random
a = random.randint(6,8)
b = random.randint(6,8)
if a>b:
	j = '전사'
elif a==b:
	j = '궁수'
else:
	j = '법사'
print(f'캐릭터 정보: 힘({a}), 지력({b})')
print(f'캐릭터 직업: {j}')
