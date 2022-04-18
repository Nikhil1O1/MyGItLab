
def binaryToDecimal(n):
    return int(n,2)

def pairCount(n):
	result = -1
	arr = []
	for r in range(n+1):
		arr.append([0 for c in range(n+1)])
	for i in range(n+1):
		for j in range(n+1):
			temp = i+j
			if arr[i][j]==0:
				if temp<=n:
					if (temp == (int(i)^int(j))):
						result+=2
						arr[i][j] = 1
						arr[j][i] = 1

	return(result%(1000000009))

#n = int(input())
a = binaryToDecimal('1111111111')
print(pairCount(a))