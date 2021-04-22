class Category:
    def __init__(self, budget_category, amount):
        self.budget_category = budget_category
        self.amount = amount

    def deposit(self, amount):
        self.amount += amount
        return f"You have deposited {amount} in your {self.budget_category} account."

    def withdraw(self, amount):
        self.amount -= amount
        return f"You have withdrawn {amount} from your {self.budget_category} account."

    def current_balance(self):
        return f"Your current balance is {self.amount}"

    def check_balance(self, amount):
        if amount >= self.amount:
            return True
        else:
            return False


food = Category("Food", 500)
clothing = Category("Clothing", 200)
transportation = Category("Transportation", 100)
rent = Category("Rent", 1000)

print(food.deposit(100))
print(food.current_balance())
