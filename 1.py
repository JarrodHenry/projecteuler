
target = range(1,1000)
summation = []
total = 0
for number in target:
	if number % 3 == 0 or number % 5 == 0:
		summation.append(number)

for number in summation:
	total = total + number

print total	
