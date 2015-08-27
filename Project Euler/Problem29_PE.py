list1 = []

for a in range(2, 101):
	for b in range(2, 101):
		list1.append(a**b)

print(len(list(set(list1))))	
