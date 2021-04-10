class Budget:

	"""

	This is a budget class that takes two(2) parameters

	1. Category: This refers to a category of the budget
				that is to be worked on e.g food, clothes

	2. Balance: This is the total amount of money budgeted
				for each category with an initial value of
				50,000

	This Class has four(4) methods apart from the __init__
	function;

	1. deposit() method: allows user to deposit funds into
						selected category and adds amount
						deposited to the balance

	2. withdraw() method: allows user to withdraw funds
						from a selected category and
						subtracts amount withdrawn from
						the balance

	3. transfer() method: allows user to transfer funds
						from one category's account to
						another category. Subtracts
						funds from the balace of thr
						giving category and adds funds
						to the balance of
						the receiving category

	4. balance() method: allows user to check the remaining
						funds in the account of a selected
						category


	USAGE:

	if ___name__ == '__main__':

		food = Budget('food')
		food.deposit()
		food.withdraw()
		food.transfer()
		food.balance()


	VIA IMPORT:

	from budget import Budget

	food = Budget('food')
	food.deposit()
	food.withdraw()
	food.transfer()
	food.balance()

	"""

	def __init__(self, category, balance=50000):

		""" initialising the class with 2 params """

		self.category = category
		self.balance = balance

	def deposit(self) -> int:

		""" deposit method; to deposit funds """

		try:
			deposit_amount = int(input("How Much Do You Want To Deposit? \n\t > "))

			if deposit_amount <= 0:
				print("You have entered an invalid amount")

			print(f"\nTransaction Successful, you have deposited\
				{deposit_amount:#,.2f} to {self.category} \n".title())

			self.balance += deposit_amount

			print(f"your current budget for {self.category} is #{self.balance:#,.2f} \n".title())

		except ValueError:
			print("You have made an invalid input. Try again")
			return self.deposit()

		return self.balance

	def withdraw(self) -> int:

		""" withdraw method to withdraw funds """

		try:
			withdraw_amount = int(input("how much do you want to withdraw? \n\t > ".title()))

			if withdraw_amount > self.balance:
				print("Transaction failed due to insufficient balance")
			print(f"\nTransaction Successful, you have withdrawn \
				{withdraw_amount:#,.2f} from {self.category} \n".title())

			self.balance -= withdraw_amount

			print(f"your current budget for {self.category} is #{self.balance:#,.2f} \n".title())

		except ValueError:
			print("You have made an invalid input. Try again")
			return self.withdraw()

		return self.balance

	def transfer(self) -> int:

		""" transfer method to transfer funds from one category to another """
		try:
			transfer_category = int(input("Enter category to transfer funds into\n \
				\t1. Food\n\t2. Clothing\n\t3. Entertainment \n\t > ".title()))
			transfer_amount = int(input("\nHow much do you want to transfer?\n\t > ".title()))

			categories = ['Food', 'Clothing', 'Entertainment']

			if transfer_category == 1:
				print("You can not transfer into the same account".title())
				return self.transfer()

			print(f"Transaction Successful, you have transfered\
				{transfer_amount:#,.2f} from {self.category} to {categories[transfer_category]}\n".title())

			self.balance -= transfer_amount

			print(f"Your current budget for {self.category} is {self.balance:#,.2f}".title())

		except ValueError:
			print("You have made an invalid input. Try again")
			return self.transfer()

		return self.balance

	def balance_cat(self) -> str:

		""" balance method to check current balance of a category """

		print(f"Your current balance for {self.category} is {self.balance}".title())
