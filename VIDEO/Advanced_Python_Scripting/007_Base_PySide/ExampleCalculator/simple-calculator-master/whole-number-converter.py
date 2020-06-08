# This module converts the given expression to its decimal equivalent
# However, this module is currently designed for whole number only
def eval(expr, base):
	digits = []
	x = len(expr) - 1
	y = 0
	while x >= 0 and y < len(expr):
		digits.append(int(expr[x]) * (base ** y))
		x -= 1
		y += 1
	return digits

total = 0
for x in eval(str(input("Enter a number to convert: ")), input("Enter base of the number: ")):
	total += x
print total