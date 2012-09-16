from __future__ import generators

def fib():
	a,b = 0,1
	while 1:
		yield a
		a,b =b, a+b

ra=fib()
total = 0

for i in range(1000):
	check = ra.next()
	if check % 2 == 0 and check < 4000000:
		total = total + check

	if total > 4000000:
		break

print total


