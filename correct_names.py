in_str=input("Enter the faulty string \n")
p_str = in_str

k=[]

for key_char in range(1, len(p_str)):
	
	
	if (p_str[key_char].isalpha() or ord(p_str[key_char])==32):
		k.append(p_str[key_char])
		

	

print("The new string is \n ")

print(''.join(k))

