my_dict={"Harsha":"best", "day":"good", "modi":"bjp"}

key_list = list(my_dict.keys())
val_list = list(my_dict.values())

print("Here is the dictionary : ", my_dict)

a = input("Enter the value to get corresponding keys : ")

print(key_list[val_list.index(a)])