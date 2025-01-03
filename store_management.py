
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

class Product:
    def __init__(self,path):
        self.welcome_message ="<<<Welcome To Store Management System>>>"
        print(self.welcome_message)
        self.path =path
        

        
    def store_operation(self,name,price,quantity): #store name price and quantity of the store
        self.name =name
        self.price =price      
        self.quantity =quantity
        
        with open(self.path,"a+") as file_obj:   #store the data in the file
            file_obj.write(self.name)
            file_obj.write(" ,")            
            file_obj.write(self.price)
            file_obj.write(" ,")
            file_obj.write(self.quantity)
            file_obj.write("\n")
                
    def add_product(self):   #add new product in the file
        pass

    def delete(self): #delete exiting product from the file
        pass

    def read_product(self):  #read product from the file
        pass
    
        
def main(): #main function
    product_obj =Product("store_management.txt") #make a object of the product class
    product_obj.store_operation("sushil","2000","12") 
    

main() #call the main function