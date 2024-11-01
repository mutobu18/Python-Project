Restaurant Management System  

Date : 31st October 2024 

Author: 168837 Kahindo Mutobu Mary 

Project Overview 
The restaurant management system streamlines restaurant operations by managing the menu, processing customer orders, and handling billings. The system includes different roles for restaurant staff such as servants, managers, and accountants, each with specific responsibilities. The goal is to automate key processes to improve efficiency and provide better service to customers.

Class description 
1.Menu class: 
Represents the food and drinks available in the restaurant. Each menu has a name, type(food/drink),and price .
•	Attributes: item_name, item_price .
•	Methods: add_item(), update_item() ,remove_item().
Subclasses: 
             Food menu class: stores information specific to food items.
            Drink menu class: stores information about specific drink items.
          
2.Customer class: 
Represents the customers placing orders.It stores  the customer ‘s information including ,name ,location and selected items.
•	Attributes :name, location,order
•	Methods: place_oder(), cancel_order(), display_customer_info()
Subclasses : 
         Online customer class: stores information about customers who order online.
        In-store customer class:stores information about customers who order online .

3.Staff class : 
Serves as the parent class for all restaurant staff, storing basic information and allowwwing role-based operations.
•	Attributes: name,staff_id, role
•	Methods: display_staff_details()
Subclasses: 

•	Manager Class: Oversees restaurant operations and ensures smooth management.
•	Servant Class: Takes orders from customers and serves them.
•	Accountant Class: Calculates bills and processes payments for customers
