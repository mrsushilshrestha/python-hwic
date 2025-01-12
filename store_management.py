
# ****Example for how it will work when run****
# Type what you want to do. (add / delete / list) : add
# product name: garcia
# product price: 200
# product quantity: 2
# Product Added successfully!


# Type what you want to do. (add / delete / list) : delete
# product name: garcia
# Product deleted successfully!

# Type what you want to do. (add / delete / list) : list
# product name => alex albon
# product price => 58000
# product quantity => 55
# product name => lewis hamilton
# product price => 88000
# product quantity => 100
# product name => garcia
# product price => 200
# product quantity => 2

#--------------------Store-Management-System----------------------------------
class Product:
    def __init__(self,path):
        self.welcome_message ="<<<Welcome To Store Management System>>>"
        print(self.welcome_message)
        self.path =path

                
    def add_product(self, name, price, quantity):  # Add a new product to the file
        self.name = name
        self.price = price
        self.quantity = quantity

        try:
            with open(self.path, "a+") as file_obj:  # Store the data in the file
                file_obj.write(f"{self.name}, {self.price}, {self.quantity}\n")

        except Exception as e:
            print(f"Exception in add_product: {e}")  # Proper exception handling

    
    def delete_product(self,delete_data): #delete exiting product from the file
        
        try:
            with open(self.path,"r+") as file_object:
                data=file_object.readline()
            
            with open(self.path,"w+") as file_obj:
                for items in data:
                    if not delete_data in items:
                        file_obj.write(items)

        except Exception as e:
            print(f"Exception in add_product: {e}")


    def read_product(self,user_search):  #read product from the file
        
        try:
            with open(self.path,"r+") as file_object:
                data=file_object.readline()
                
        
            for items in data:
                if user_search in items:
                    return items

        except Exception as e:
            print(f"Exception in add_product: {e}")


    
        
#---------Main-Function-------------------------------------   
    
def main(): #main function
    product_obj =Product("store_management.txt") #make a object of the product class

    option =input("Type what you want to do. (add / delete / list) :")
    if option=="add":
        product_obj.add_product(name="Sushil", price=1000, quantity=10)

    elif option=="delete":
        product_obj.delete_product(delete_data='sushil')

    elif option=="list":
        user_result=product_obj.read_product(user_search="Sushil")
        print(user_result)

    

main() #call the main function