in_str = input("Enter the faulty string : \n")

# in_str = "HarshaIsTheBest"
in_str = "{} A".format(in_str)


p_str = in_str

k=[]
ptr = 0

for key_char in range(1, len(p_str)):
	
	
	if p_str[key_char].isupper() :
		k.append(p_str[ptr:key_char])
		ptr = key_char

	

print("The new string is \n ")

print(' '.join(k))
