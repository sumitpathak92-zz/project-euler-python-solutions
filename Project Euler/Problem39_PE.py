res = 0
resSol=0
for i in range(2, 1001, 2):
	noOfSol=0
	for j in range(2, i/3):
		if(i*(i-2*j))%(2*(i-j)) == 0:
			noOfSol+=1
	if noOfSol>resSol:
		resSol=noOfSol
		res=i

print(res)				