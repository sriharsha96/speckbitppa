def func_try():
	print("This is a program to compute 5/0 and check for an exception")

	a=5
	b=0
	c=5/0

	return c



try:
	func_try()
except ZeroDivisionError:
	print("It's a zero division error")
else:
	print("Everything is fine")
