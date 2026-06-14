#!/usr/bin/env python3
class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transaction = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if type(value) is int and 0 <= value <= 100:
            self._discount = value
        else:
            raise ValueError("Not valid discount")

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity
        # Add item once per quantity (fix for multiples test)
        self.items.extend([item] * quantity)
        self.previous_transaction.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        # Fix: check if discount is 0, not if transactions are empty
        if self.discount == 0:
            print("There is no discount to apply.")
            return
        self.total *= (1 - self.discount / 100)
        print(f"After the discount, the total comes to ${int(self.total)}.")

    def void_last_transaction(self):
        if not self.previous_transaction:
            return
        last = self.previous_transaction.pop()
        self.total -= last["price"] * last["quantity"]
        # Remove all instances of that item added in that transaction
        for _ in range(last["quantity"]):
            self.items.remove(last["item"])