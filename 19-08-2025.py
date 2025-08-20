# 3.Base class: Order with method process_order().
# Derived classes:
# OnlineOrder – overrides to include payment and shipping.
# StorePickupOrder – overrides to include in-store pickup instructions.



# class shopping:
#     def process_order(self):
#         return"Happy Shopping "
# class online_order(shopping):
#     def process_order(self):
#         return super().process_order(),"You choose a online payment & shipping"
# class store_pickup(shopping):
#     def process_order(self):
#         return super().process_order(), "You choose a  Store Pickup "

# o=online_order()
# print(o.process_order())
# s=store_pickup()
# print(s.process_order())

# --------------------------------------------------------------------


# 3. Create a subclass Car that inherits from Vehicle. 
#    Car's __init__ should take make, model, year, and an additional attribute num_doors. 
#    Use super() to call the Vehicle's __init__ to handle the inherited attributes. 
#    Override the get_info() method to also include the number of doors. Use super() to call the parent's get_info() and append the new information.


class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}"

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def get_info(self):
        parent_info = super().get_info()
        return f"{parent_info}, Doors: {self.num_doors}"
    
m = Vehicle('audi','20LKM',2016)
n = Car('panzer','56GM',2013,5)
print(m.get_info())
print(n.get_info())