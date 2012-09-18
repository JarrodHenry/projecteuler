

def buildlist():
	pythaglist=[]
	for a in range(1,1001):
		for b in range(1,1001):
			for c in range(1,1001):
				if a+b+c == 1000 and a < b < c:
					pythaglist.append([a,b,c])

	return pythaglist


def main():
	pythaglist = buildlist()

	for testset  in pythaglist:
		a= testset[0]
		b= testset[1]
		c= testset[2]

		if  pow(a,2) + pow(b,2) == pow(c,2):
			print a,b,c,a*b*c
			break
		

if __name__=='__main__':
	main()
