class Menu:

#Initialize a list of the menu items 

      def __init__(self):

          self.__items=[] #private attribute 
  
 #Methods  to add new item in the menu using data structure 

      def add_item(self,item_name,item_price):
   
          item={
      
      'name': item_name,
      'price':item_price
   }

          self.__items.append(item)

   #Method to  view the list or the menu  if the menu exist

      def  view_menu(self):
         for item in self.__items:
       
           print(f"{item['name']}:${item['price']:.2f}")

   #method to update an item 

      def update_item(self,new_name=None,new_price=None):
     #If the item is on the list
           for item in self.__items:
       
            if item['name']== item:
         
             if new_name:
           
              item['name']= new_name

              if new_price is not None:#Updating price
             
                item['price']= new_price
             #Update changes  the new items list 

             print(f"Updated {item} to {item['name']} at ${item['price']:.2f} ") 


      def delete_item(self,item_name):
     #If the item is the list

          for item in self.__items:
       
           if item['name']== item_name:
         
            self.__items.remove(item)

            print(f"Removed item:{item_name}")

    #Getter method to retrive the list of items 

      def get_items(self):
  
          return self.__items
      
      #Inheritance from the menu class 
#handling exceptions for adding an item
class FoodMenu(Menu):
    
    #Override 
    def add_item(self,item_name,item_price):
       if item_name.lower() not in ['water','soda','juice']:
          
          super().add_item(item_name,item_price)

       else:
          print(f"{item_name} is a drink ,not food. ")


class DrinkMenu(Menu):

   #Override 
   def add_item(self,item_name,item_price):
      
      if item_name.lower() in ['Tea','soda','juice']:
         
         super().add_item(item_name,item_price)

      else: 
         
         print(f"{item_name}is food not drink")


#Creating an object for the Menu class 

food_menu= FoodMenu()
drinkmenu= DrinkMenu()

#Adding  items 

food_menu.add_item("Chips",240)
food_menu.add_item("Rice",500)
food_menu.add_item("Pizza",2000)
food_menu.add_item("bugger",1000)
drinkmenu.add_item("juice",100)
drinkmenu.add_item("water",50)
drinkmenu.add_item("soda",200)

       
#view menu 

print("Food Menu:")

food_menu.view_menu()

print("\nDrink Menu:")
drinkmenu.view_menu()



     