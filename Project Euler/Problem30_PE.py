l = []
for i in range(2, 354294):
	i = str(i)
	Sum = 0
	for dig in i:
		Sum = Sum + int(dig)**5
	if Sum == int(i):
		l.append(Sum)

ans= sum(l)
print(ans)
