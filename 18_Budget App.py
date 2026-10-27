class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description = ''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description = ''):
        if not self.check_funds(amount):
            return False
        self.ledger.append({'amount': (amount*-1), 'description': description})
        return True

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, Destination):
        if not self.check_funds(amount):
            return False
        self.withdraw(amount, f'Transfer to {Destination.name}')
        Destination.deposit(amount, f'Transfer from {self.name}')
        return True

    def check_funds(self, amount):
        if self.get_balance() < amount:
            return False
        return True

    def __str__(self):
        output = self.name.center(30, '*') + '\n'
        for entry in self.ledger:
            output += (
                f"{entry['description'][:23]:<23}"
                f"{entry['amount']:>7.2f}\n"
            )
        output += f"Total: {self.get_balance():.2f}"
        return output


        max_length = max(len(str(cat)) for cat in categories)

        for row in range(max_length):
            output += '    '
            for cat in categories:
                name = str(cat)
                output += (name[row] if row < len(name) else ' ') + '  '
            output = output.rstrip() + '\n'


def create_spend_chart(categories):
    total_spent = 0
    category_spent = []

    for category in categories:
        spent = sum(-item["amount"] for item in category.ledger if item["amount"] < 0)
        category_spent.append(spent)
        total_spent += spent
    
    percentages = [
        int(spent / total_spent * 100) // 10 * 10
        if total_spent > 0 else 0
        for spent in category_spent]
    
    chart = "Percentage spent by category\n"
    for level in range(100, -1, -10):
        chart += str(level).rjust(3) + "|"
        for percentage in percentages:
            chart += " o " if percentage >= level else "   "
        chart += " \n"
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"
    
    max_length = max(len(category.name) for category in categories)
    for i in range(max_length):
        chart += "     "
        for category in categories:
            chart += (
                category.name[i] if i < len(category.name) else " "
            ) + "  "
        chart += "\n"
    
    return chart.rstrip("\n")



food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)
list=[food]
print(create_spend_chart(list)) 