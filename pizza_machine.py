import time


price_table =   { 3: 50,  4:80,  5:40,  6:60,  7:60,   8:20,   9:60,  10:60, 11:20 , 12:20 , 0:0 }
menu_table = { 0: "No BEVERAGE", 3:"Base-Thin Crust" , 4:"Base-Cheese-crust" , 5:"Base : Regular" , 6: "Beverage : Coca cola", 7: "Mountain dew 	", 
	8: "Water bottle 	", 9:"Extra cheese 	",10: "Corn + Onion 	", 11.:"Chicken + Olives", 12:"Paneer + Capsicum"    }

	
cart=[]

def basic_menu():
	print("\n \n================ PIZZA MACHINE ================")
	print("1. Make  a customized Pizza \n2. Order only a beverage \n \n")


def pizza_menu():
	print("-------- Choose a base --------\n")
	print("3. Thin Crust    ------------> Rs 50 ")
	print("4. Cheese Crust  ------------> Rs 80 ")
	print("5. Regular       ------------> Rs 40 ")
	print("\n")


def drinks_menu():
	
	print("-.-.-.-. Choose a beverage (Multiple options permitted) .-.-.-.-\n")
	print("6. Coca cola (330 ml)_____________Rs 60 ")
	print("7. Mountain dew (330 ml)__________Rs 60 ")
	print("8. Water bottle (500ml)___________Rs 20 ")
	print("PRESS 0 for no beverage")

	print("\n")

def toppings():

	print("-.-.-.-. Choose toppings (Multiple options permitted) .-.-.-.-\n")
	print("9.  Extra cheese  -------> Rs 60 ")
	print("10. Corn + Onion   ------> Rs 60 ")
	print("11. Chicken + Olives  ---> Rs 20 ")
	print("12. Paneer + Capsicum ---> Rs 20 ")
	print("\n")


def preorder():

	print("\nYour order so far : ")
	print("CODE 			ITEM 				PRICE")
	for i in cart:
		print(i ," 			", menu_table[i],"		", price_table[i])


def pricing():
	total = 0	
	for i in cart:
		total=total+price_table[i]
	print("---------------")
	print("TOTAL : ",total," INR")
	print("---------------")
	print("Have a nice day ! ")
	print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")


print("This is a basic PIZZA vending machine installed at SPECKBIT")
print("An employee walks to the machine, selects a PIZZA , customizes the Pizza, chooses beverage of his/her choice \nand the machine shows total amount payable. ")
print("Due to technical limitations , the Pizza is a list with all the chosen toppings. ")






while True:
	
	basic_menu();
	basic_inp = int(input("Your choice : "))



	if basic_inp == 1:
		pizza_menu();
		pizza_inp = int(input("Your choice : "))
		cart.append(pizza_inp)
		print("\n")

		toppings();
		top_list = list(map(int,input("Your choice of toppings : ").strip().split()))
		cart=cart+top_list	
		print("\n")

		drinks_menu();
		drinks_list = list(map(int,input("Your choice of Drinks : ").strip().split()))
		cart=cart+drinks_list
		print("\n")
		


	elif basic_inp == 2: 
		drinks_menu();
		drinks_list = list(map(int,input("Your choice of Drinks : ").strip().split()))
		cart=cart+drinks_list
		print("\n")
		preorder();




	else : 
		print("Please start over, you entered a wrong choice. \n")
		break


	print("\nHere is your bill : ")
	print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
	preorder();
	pricing();
	print("\n")
	break
















