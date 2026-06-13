#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        self.size = size
        self.price = price

    @property
    def size(self):
        # getter for size
        return self._size
        
    @size.setter
    def size(self, value):
        # Setter for size that ensures it matches allowed size
        allowed_sizes = ["Small", "Medium", "Large"]
        if value in allowed_sizes:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")
            self._size = None

    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price += 1                