# bin = "{0:b}".format(178955)
# print(bin)
l=[]

def checkPalindrome(n):
	n = str(n)
	if n == n[::-1]:
		return True
	else:
		return False

# def reverseStr(str):
# 	for c in reversed(str):
# 		return c

for i in range(1, 1000001):
	bin_i = "{0:b}".format(i)
	#print(bin_i)
	if checkPalindrome(i)==True and checkPalindrome(bin_i)==True:
		l.append(i)
		continue

#print(l)
print(sum(l))		
