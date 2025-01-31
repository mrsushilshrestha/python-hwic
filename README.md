# Store Management System

#### Description

The Store Management System is a Python-based application designed to manage store inventory. It enables users to add, delete, and read product details stored in a text file. This simple yet functional system ensures efficient management of inventory operations.

#### Features

- **Add Product**:
  - Add new products with details like name, price, and quantity.
  - Persist data to a file for future use.
- **Delete Product**:
  - Remove products from the inventory by name.
  - Confirms whether the product was deleted or not found.
- **Read Product**:
  - Search and display specific product details.
- **Exit**:
  - Exit the application gracefully.

#### How It Works

- The program stores product information in a file named `store_management.txt`.
- The format for storing data is:
  ```
  product_name, product_price, product_quantity
  ```
- Users interact with the program through text-based prompts.

#### Usage Instructions

1. **Run the Script**: Execute the Python file to start the system.
2. **Choose an Operation**:
   - **Add Product**:
     - Select option `1` or type `add`.
     - Enter product details as prompted.
     - A success message confirms the addition.
   - **Delete Product**:
     - Select option `2` or type `delete`.
     - Enter the product name to delete.
     - The program informs if the product was successfully deleted or not found.
   - **Read Product**:
     - Select option `3` or type `read`.
     - Provide the product name to search.
     - Details are displayed if the product exists.
   - **Exit Program**:
     - Select option `4` or type `exit` to terminate the program.
3. **Continue or Exit**:
   - After each operation, the program prompts whether to continue or exit.

#### Example Interaction

##### Adding a Product:

```
You selected add.
Enter the Name: Pen
Enter the Price: 10
Enter the Quantity: 100
Product Added successfully!
```

##### Deleting a Product:

```
You selected delete.
Enter the Name for delete: Pen
Product deleted successfully!
```

##### Reading a Product:

```
You selected read.
Enter the Name For Search: Pen
Pen, 10, 100
```

##### Exiting the Program:

```
Exiting...
System Out...
```

#### Error Handling

- Handles file access errors and invalid inputs gracefully.
- Provides clear error messages when issues occur.

#### Requirements

- Python 3.x

#### Notes

- Ensure the `store_management.txt` file is in the same directory as the script. If not, the program will create it.
- The search operation is case-sensitive.

#### Acknowledgment

This project is an assignment for the training program at **Himalayan Whitehouse International College**.
