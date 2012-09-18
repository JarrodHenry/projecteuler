

def checknumber(number):

	divisor = 20
	
	while divisor > 0:
		if number % divisor != 0: return False
		divisor = divisor - 1


def main():
	number = 1
	while checknumber(number) == False:
		number = number + 1

	print number

if __name__ == '__main__':
	main()

