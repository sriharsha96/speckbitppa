in_str = input("Enter password string : ")


flag_lower = 0
flag_upper = 0
flag_num = 0
flag_len = 0
flag_special = 0

print("length is  : ", len(in_str))
print("=================================")

k = len(in_str)

if k in range(8,16):
	flag_len = True


for i in range(0, len(in_str)):
	
	y = ord(in_str[i])
	print("Key is : ",y)
	
	if  y in range(97,122):
		flag_lower = True

	if y in range(65,90):
		flag_upper = True

	if y in range(48,57):
		flag_num = True

	if y==35 :
		flag_special = True

	if y==64:
		flag_special = True
	
	if y==36:
		flag_special = True


print("=================================")
print("flag_len = ",flag_len)
print("flag_lower = ",flag_lower)
print("flag_upper = ",flag_upper)
print("flag_num = ",flag_num)
print("flag_special = ",flag_special)

if (flag_special==True and flag_num==True and flag_upper==True and flag_lower==True and flag_len==True):
	print("\nPassword is in compliance")

else : 
	print("\nPassword is NOT in compiance")




