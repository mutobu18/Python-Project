class Staff:

    #Initialize the Staff class 

    def __init__(self,name,__staff_id,role):

        self.name=name
        self.__staff_id=__staff_id
        self.role=role

#Display details of the staff 

    def display_details(self):

        print(f"Staff Id:{self.__staff_id},Name:{self.name},Role:{self.role}")

    #Getter method for the staff_id attribute 
         
    def get_staff_id(self):
        return self.__staff_id

class Servant(Staff):

    def __init__(self, name, staff_id):
        super().__init__(name, staff_id, role="Servant")
        self.order_status = "Pending"

        #override 

    def display_details(self):

        print(f"Staff Id:{self.__staff_id},Name:{self.name},Role:{self.role}")


    # Take order from a customer
    def take_order(self, order):
        print(f"Order taken: {order}")
        self.order_status = "In Progress"

    #order served 

    def serve_order(self,order):
        print(f" order served:{order}")
        self.order_status="Order served "

        
        
class Manager(Staff):

    def __init__(self,name,staff_id):

        super().__init__(name,staff_id,role="Manager")

        #Oversee restaurant operations

        print(f"Manager{self.name} is overseeing operations in the restaurant")

    #override 

    def display_details(self):

        print(f"Staff Id:{self.__staff_id},Name:{self.name},Role:{self.role}")




class Accountant(Staff):

    def __init__(self,name,staff_id):

        super().__init__(name,staff_id,role="Accountant")

        #Generate bill for a customer 

        def generate_bill(self,amount):

            print(f"Bill generated: ${amount:.2f}")


            def  process_payment(self,amount):

                print(f"payment of ${amount:.2f} proceed by {self.name}.")

    #override 

    def display_details(self):

        print(f"Staff Id:{self.__staff_id},Name:{self.name},Role:{self.role}")




#Creating an object of the class 


sev1= Servant("John",101)
sev2=Servant("Mary",102)
sev3=Servant("lucy",103)
sev4=Servant("Paul",104)
mang=Manager("Sipora",100)
acc=Accountant("Nelly",105)


#Display staff details 

sev1.display_details()
sev2.display_details()

#Take an order 

sev1.take_order()




    



    