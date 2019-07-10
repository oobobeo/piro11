a = []
for i in range(9):
	a.append(int(input()))

total = sum(a)

import random
while True:
	x,y = random.randint(0,8), random.randint(0,8)
	if total-a[x]-a[y]:
		a.remove(a[x])
		a.remove(a[y])
		for i in a:
			print(i)
		break