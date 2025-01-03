# import os
class Computer_shop:

    def __init__(self,path): 
        self.path =path

    def write_function(self,name,brand,id): #wite function 
        self.name =name
        self.brand =brand
        self.id =id

        with open(self.path,"a+")as file:
            file.write(self.name+", ")
            file.write(self.brand+", ")
            file.write(self.id) 
            file.write("\n")           

    def read_function(self,word): #read function
        with open(self.path,"r")as file:
            data = True
            # line=1
            while data:
                data=file.readline()
                if word in data:
                    print(data)
                    return
                else:
                    # line+=1
                    pass
            return print("Not Found!!!")     

    def update_function(self,old_name,update_name): #update function
        self.old_name = old_name
        self.update_name =update_name
        

        # with open(self.path,"a+")as file: #to update and Read data using the [a+] append mode
        #     file.write(self.update_name+", ")
        #     file.write(self.update_brand+", ")
        #     file.write(self.update_id+", ")
        #     file.write("\n")
        
        with open(self.path,"r") as f:
            data =f.read()            
            new_data=data.replace(self.old_name,self.update_name) 
            # print(new_data) 
        
        with open(self.path,"w+") as f:
            f.write(new_data)
            

    #Delete line
    #Internet Reference
    #some Contant idea take from internet
    def delete_function(self, word):  # Delete function
        with open(self.path, "r") as file:
            lines = file.readlines()  # Read all lines from the file

        with open(self.path, "w") as file:
            found = False
            for line in lines:
                if word not in line:  
                    file.write(line)  # Write back lines that don't contain the word
                else:
                    found = True  # Mark the word as found and skip writing this line
        
        if found:
            print(f"Entries containing '{word}' have been deleted successfully!")
        else:
            print(f"No entries containing '{word}' were found.")



#---------value passing section------------------------------------------------------
def main():
    command ="y"
    while command=="y":
        message="""
        Enter the Option
        1>Write Data
        2>Read Data
        3>Update Data
        4>Delete Data 
        """    

        option =input(message)
        path ="Computer_shop.txt"
        computer_shop_obj =Computer_shop(path)

        #condition for Operations
        if option=='1': #Write data
            print("Enter the Required Data... ")
            name =input("Enter the Name Of Customer:- ")
            brand =input("Enter the Brand Of Computer:- ")
            id =input("Enter the Id of Customer:- ")
            computer_shop_obj.write_function(name,brand,id)

        elif option=='2': #for read data
            word=input("Enter the Name to search: ")
            computer_shop_obj.read_function(word)
            
        elif option=='3': #for read data
            print("You Click Update Option...")
            old_name =input("Enter the Old Name Of Customer: ")
            update_name =input("Enter the Name Of Customer: ")    
            computer_shop_obj.update_function(old_name,update_name)
            
        elif option == '4':  # Delete data
            word = input("Enter the word or name to delete entries: ")
            computer_shop_obj.delete_function(word)

        else:
            print("Invalid Option !!!")

    
        command=input("Do you want to Continue y/n ").strip()  #strip() remove the whitespace
        if not command=="y":
            print("<<<<<Exit From The System>>>>>")

main()