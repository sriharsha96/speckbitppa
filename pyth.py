import math




print("This is map. The point is now at (0,0)")
print("Example Inputs  UP 10 	DOWN 20		LEFT 5		RIGHT 78 \n")


def input_data():
	a = input("-> ")
	inputmat=(a.split(" "))
	return inputmat




def dist(x,y):
	k = (x*x)+(y*y)
	l = math.sqrt(k)
	#l= math.ciel(l)
	#print("in func : k : ",k)
	#print("in Func : ",l)
	return l
		

x= 0
y = 0



while True:
	
	ops = input_data()
	arg1 = ops[0]
	arg2 = int(ops[1])


	if arg1 == "UP":
		y=y+arg2
		

	if arg1 == "LEFT":
		x=x-arg2

	if arg1 == "DOWN":
		y=y-arg2

	if arg1 == "RIGHT":
		x=x+arg2
	
	print("x and y are : ",(x,y))
	value= dist(x,y)
	print("x and y are : ",(x,y))
	print("Rounded off Distance from  (0,0) is ",value)
	print("\n")