#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []
        self.last_transaction_amount = 0

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.last_transaction_amount = price * quantity
        for _ in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        if self.discount:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.last_transaction_amount

register = CashRegister()
register.add_item("apple", 1.00, 3)
register.add_item("banana", 0.50, 2)
register.apply_discount()
register.void_last_transaction()
print(register.total)  # Should print the total after applying the discount and voiding the last transaction
# This code defines a CashRegister class that can add items, apply discounts, and void the last transaction.