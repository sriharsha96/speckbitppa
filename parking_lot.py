import time

class Spaces:
	def __init__(self, type=4,vehicle_no=0,time_entry=0,time_exit=0):
		print("intiatialising new account")
		self.type=type
		self.vehicle_no=vehicle_no
		self.time_exit=time_exit
		self.time_entry=time_entry


ledger = {}
space2 = 2
space4 = 2



while True:

	if space2<=0:
		print("Not enough spaces, Please come later")

	if space4<=0:
		print("Not enough spaces, Please come later")

	print("Welcome to parking lot ! ") 
	print("Available 2 Wheeler spaces : ",space2)
	print("Available 4 Wheeler spaces : ",space4)
	

	print("\nEnter an option. \n 1. Enter/Exit the space \n 2. Show statistics \n")

	choice = int(input("Enter choice - "))
	print("\n \nThanks, your choice is - ",choice)

	

	if choice==1:
		print("\n====You want to Enter / Exit ===\n")
		print("Enter an option. \n 3. Enter  \n 4. Exit \n")
		sec_choice = int(input("Enter second input : "))
		print("\n \nYour new choice is - ",sec_choice)
		if sec_choice==3:
			v_type = int(input("Enter 2 for 2 wheeler and 4 for 4 wheeler : "))
			if v_type == 2:
				space2 = space2-1
			
			elif v_type == 4:
				space4 = space4-1

			v_num = input("Enter vehicle number : ")
			time_in = time.ctime()
			vehicle = Spaces(v_type,v_num,time_in)
			ledger[v_num] = vehicle
		
		elif sec_choice==4:
			v_num2 = input("Exit, what's the vehicle number ? : ")
			vehicle = ledger[v_num2]
			vehicle.time_exit=time.ctime()

			print("You're going :")
			print(vehicle.type ,vehicle.vehicle_no , vehicle.time_entry , vehicle.time_exit )
			if vehicle.type == 2:
				space2 = space2+1
			
			elif vehicle.type == 4:
				space4 = space4+1

			
			if v_num2 in ledger:
				del ledger[v_num2]
			else:
				print("Vehicle not found\n")

			
	elif choice==2:
		print("\n Here are the available data :\n")
		print(ledger)

	

	else:
		print("\n =====================Thank you for your visit. ===================\n")
		break




