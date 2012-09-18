

def isPalindrome(number):
	numberstring = str(number)
	right = numberstring[0:3]
	left = numberstring[3:6]
	
	return left == right[::-1]


def main():
	# first, let's just see all the palindromes
	
	x = 100000
	top= 999
	highest = 0
	palindrome = [] 

	while (x < 998001):
		if isPalindrome(x):
			palindrome.append(x)	
		x= x+1
		
	for number in palindrome:
		divisor = 999
		while divisor > 100:
			if number % divisor == 0:
				if number / divisor < 1000:
					if number > highest:
						highest = number	
			divisor = divisor - 1 

	print highest

if __name__ == '__main__':
	main()

