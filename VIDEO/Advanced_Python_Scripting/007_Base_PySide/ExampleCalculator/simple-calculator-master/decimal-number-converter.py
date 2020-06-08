# This module was designed to convert numbers after
# the decimal point to its decimal equivalent
def eval(expr, base):
	digits = []
	x = len(expr) - 1
	y = -1
	while x >= 0 and (abs(y) - 1) < len(expr):
		digits.append(float(expr[x]) * (float(base) ** y))
		x -= 1
		y -= 1
	return digits

total = 0
for x in eval(str(input("Enter a number to convert: ")), input("Enter the base of the number: ")):
	total += x
print total