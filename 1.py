
target = range(1,1000)
total = 0
for number in target:
	if number % 3 == 0 or number % 5 == 0:
		total = total + number

print total	
