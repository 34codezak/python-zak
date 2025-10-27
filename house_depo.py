def calc_depo():
	try:
		# Handle input functionality separately
		name = input("Insert your name: ")
		credit = float(input("Enter your credit amount: "))
		value = float(input("Enter the value of the property: "))
		
		if credit <= 0 or value <= 0:
			raise ValueError("Amounts must be greater than zero.")

		deposit_percent = (credit / value) * 100
		print(f"{name}, your deposit covers {deposit_percent:.2f}% of the house price.")
		print(f"This is your deposit amount you'll pay: {deposit}")

		if credit >= 100_000:
			print("You have a strong financial positon!")
		elif deposti_percent >= 20:
			print(f"{name}, that's a solid deposit ratio")
		else:
			print(f"{name}, your deposit is below 10%. There are other financial options available.")

		return deposit_percent

	except ValueError as e:
		print("Error:", e)
		return None

# Run the function interactively
if __name__ == "__main__":
	calc_depo()
