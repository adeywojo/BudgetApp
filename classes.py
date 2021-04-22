class Category:
    def __init__(self, amount, category):
        self.category = category
        self.budget_category = []
        self.amount = amount

    def deposit(self, amount, budget_category):
        self.amount += amount
        return f"You have deposited ${amount} in your {budget_category} account."

    def withdraw(self, amount, budget_category):
        self.amount -= amount
        return f"You have withdrawn ${amount} from your {budget_category} account."

    def current_balance(self):
        return f"Your current balance is ${self.amount}"

    def check_balance(self, amount):
        if amount <= self.amount:
            return True
        else:
            return False

    def transfer(self, budget_category, amount):
        if not self.check_balance(amount):
            return False
        else:
            name = input('Enter budget category: \n')
            self.budget_category = name
            self.withdraw(amount, self.category)
            self.deposit(amount, budget_category)
            return f"Transfer of ${amount} to {self.budget_category} successful."


food = Category(500, "food")
clothing = Category(200, "clothing")
transportation = Category(100, "transportation")
rent = Category(1000, "rent")

print(food.deposit(100, 'food'))
print(food.current_balance())
print(food.transfer(rent, 20))
