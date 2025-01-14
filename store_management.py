#--------------------Store-Management-System----------------------------------
class Product:
    def __init__(self,path,message):
        self.welcome_message = message
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

    
    def delete_product(self, delete_data):  # Delete an existing product from the file
        try:
            with open(self.path, "r") as file_object:
                lines = file_object.readlines()  # Read all lines from the file

            with open(self.path, "w") as file_object:
                found = False
                for line in lines:
                    if delete_data not in line:
                        file_object.write(line)  # Write back lines that do not match
                    else:
                        found = True
                if found:
                    print("Product deleted successfully!")
                else:
                    print("Product not found!")
        except Exception as e:
            print(f"Exception in delete_product: {e}")


    def read_product(self,user_search):  #read product from the file
        
        try:
            with open(self.path,"r+") as file_object:
                lines=file_object.readlines()
        
            for line in lines:
                if user_search in line:
                    return (line.strip())

        except Exception as e:
            print(f"Exception in add_product: {e}")


#---------Main-Function-------------------------------------  
def main(): #main function
    path = "store_management.txt" #path for store the data in file

    welcome_message = """
    <<<-----Welcome To Store Management System----->>>"""   #welcome message for top

    message ="""
    <<<Enter The Option [1,2,3] To Perform Operation>>>  
    1.ADD
    2.DELETE
    3.READ 
    4.EXIT
    """ #message for Input Option
    
    command ="1" 
    while command=="1" :
        product_obj =Product(path,welcome_message) #make a object of the product class
        
        option = input(message)
        
        if option == "1" or option == "add":
            print("You selected add.")
            name =input("Enter the Name: ")
            price =input("Enter the Price: ")
            quantity =input("Enter the Quantity: ")
            product_obj.add_product(name, price, quantity)

        elif option == "2" or option == "delete":
            print("You selected delete.")
            delete_data =input("Enter the Name for delete: ")
            product_obj.delete_product(delete_data)

        elif option == "3" or option == "read":
            print("You selected read.")
            user_search = input("Enter the Name For Search: ")
            user_result=product_obj.read_product(user_search)
            print(user_result)
            
        elif option == "4" or option == "exit":
            print("Exiting...")
            break
        else:
            print("Invalid Option !!!")
            continue
        
        
        system_option =input("Do You Want To Continue 1/0 for yes or no ")
        if system_option=="1" or system_option=="yes":
            command=="1"
        elif system_option=="0" or system_option=="no":
            print("System Out...")
            exit()
        else:
            # print("Please Select Valid Option[yes/no]")
            pass
                
                
main() #call the main function