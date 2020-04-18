n = 3
print('=========== USN Database ===========')

dicti = {}
while (n>0):
	
	name = input("\n Enter unique name : ")
	usn  = input("\n Enter unique USN : ")
	dicti[name] = usn
	n=n-1

print('The data is : ')

print(dicti)

for x in dicti:
	print (x,':',dicti[x])
