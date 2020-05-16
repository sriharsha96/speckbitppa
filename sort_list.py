# magicnum = input("Enter data here : ")

# # magiclist = list(map(magicnum))
# # magiclist.sort()


# # print("The list is ",magiclist)

# # x = int(input("What's the nth smallest element you wish to see ? : "))

# # print("The element is : ", magiclist[x])


def list_srt():
	n = int(input("Enter the size of list : "))
	numList = list(map(int, input("Enter the list numbers separated by space : ").strip().split()))


	print("User List: ", numList)
	numList.sort()
	print("After sorting : ",numList)
	x = int(input("Enter the Nth lowest you wish to see : "))
	return numList[x-1]

print("The element is : ",list_srt())

