class Complete:
	def __init__(self,numb=3, message="AA", status="AA"):
		self.message=message
		self.status=status
		self.numb=numb



ledger={}

while True:

	print("This is a to-do list program")

	print("1. Create a task \n2. Change the status of a specific task\n3. Show everything")
	
	choice= int(input("Your choice : "))

	print("========================")

	if choice==1:
		number=int(input("What's the task number ? : "))
		message_text=input("What's the task ? : ")
		status_text = input("Press \nTODO - If this is a to-do. \nDONE - If this is already done -> ")
		task = Complete(number,message_text,status_text)
		ledger[number] = task
		

	elif choice ==2:
		sec_choice=int(input("Enter 5 to delete an existing task \nEnter 6 to change the status of the task -> "))
		

		if sec_choice==5:
			third_choice=int(input("Enter the number of the task you wish to modify : "))
			task = ledger[third_choice]
			if third_choice in ledger:
				del ledger[third_choice]
			else:
				print("Task not found\n")

		elif sec_choice==6:
			third_choice=int(input("Enter the number of the task you wish to modify : "))
			task = ledger[third_choice]
			task.status=input("What's the NEW status of this task ? ====> ")

	elif choice ==3:
		print(ledger)
	else:
		print("Wrong choice, try again. \n")

