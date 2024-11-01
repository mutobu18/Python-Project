class Customers:

    #initialization 
    def __init__(self, name, location, order):
        self.__name = name
        self.__location = location
        self.__order = order

        #Getter and setter methods for the private attributes 

    def get_name(self):
        return self.__name

    def get_location(self):
        return self.__location
    
    def get_order(self):
        return self.__order
    
     # Method for placing or updating an order
    def place_order(self, new_order):
        self.__order = new_order
        print(f"Order placed: {self.__order}")


     # Method for canceling an order
    def cancel_order(self):
        if self.__order:
            print(f"Order '{self.__order}' has been canceled.")
            self.__order = None
        else:
            print("No order to cancel.")
    
    #Display customer info 
    
    def display_info(self):
        print(f"Customer Name: {self.__name}, Location: {self.__location}, Order: {self.__order}")

        #Online customer inherit from the customer class 

class Online_customers(Customers):
    def __init__(self, name, location, order, delivery_address):
        super().__init__(name, location, order)
        self.delivery_address = delivery_address  # Additional attribute for online customers

    def display_info(self):
        super().display_info()  # Call the base class method
        print(f"Delivery Address: {self.delivery_address}")

class In_store_customers(Customers):
    def __init__(self, name, location, order, table_number):
        super().__init__(name, location, order)
        self.table_number = table_number  # Additional attribute for in-store customers

    def display_info(self):
        super().display_info()  # Call the base class method
        print(f"Table Number: {self.table_number}")

# Example Usage
online_customer = Online_customers("Alice", "123 Online St", "Pizza", "456 Delivery Rd")
in_store_customer = In_store_customers("Bob", "789 Store Ave", "Burger", 5)

# Displaying customer information
print("Online Customer Details:")
online_customer.display_info()

print("\nIn-store Customer Details:")
in_store_customer.display_info()

online_customer.place_order()