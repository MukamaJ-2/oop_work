class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f"Name: {self.name}\nAddress: {self.address}"
    
customer1 = Customer("JOSEPH MUKAMA", "UCU, MUKONO")
print(customer1)