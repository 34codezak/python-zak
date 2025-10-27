def calc_depo(self, credit):
	try:
		name = input("Enter Your Name: ")
		credit = float(input("Add Your Credit Amount."))


		if credit <= 0:
			raise ValueError("Credit must be at least $1.")
		
		deposit = credit / 1000000 * 100
		print(f"Your deposit calculation: {deposit:.2f}")
		if credit >= 100000:
			print(f"{name}, you have good credit! Now you can go ahead and place your downpayment.")
		else:
			print("Your credit is less than the needed.")
			print("Process stopped!")
	except ValueError as e:
		print("Error: ", e)

calc_depo(50, 1000000)
