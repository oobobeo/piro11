import copy
a = ['apple','apps','apee']

result = []
for i in range(len(min(a,key=len))):
	letters = []
	for word in a:
		letters.append(word[i])
	try:
		result.append(letters[0])
		temp=copy.deepcopy(letters)
		for j in temp:
			letters.remove(temp[0])
	except:
		# print('e')
		if result:
			result.pop()
		break
	# print(result)
	

print(''.join(result))