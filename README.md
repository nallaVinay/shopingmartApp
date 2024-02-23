Shopping Application Readme
Overview
This Python script is a shopping application that facilitates various operations such as viewing products, shopping, managing a shopping cart, and checkout. It utilizes a text file (ProductsData.txt) to store product data and implements functionalities to manipulate this data and perform shopping operations.

Requirements
Python 3.8
Libraries: sys, re, pickle
Features
View Products: Display available products along with their details such as ID, name, price, and category.
Shop: Add products to a shopping cart, remove products from the cart, view the contents of the cart, and clear the cart.
Checkout: Calculate the total amount of items in the shopping cart, apply discounts if applicable, and display the checkout information.
Add a Product: Add new products to the product database with unique IDs, names, prices, and categories.
Delete a Product: Remove a product from the product database based on its ID.
Usage
Running the Application:

Ensure Python is installed on your system.
Run the script using the command: python script_name.py
Menu Options:

The application presents a menu with different options:
1: View Products
2: Shop
3: Checkout
4: Add a Product
5: Delete a Product
0: Exit
Shopping:

While shopping, users can add products to their cart, remove products from the cart, view the cart, and clear the cart.
Checkout:

Upon checkout, the application calculates the total amount of items in the cart, applies discounts (if applicable), and displays the checkout information.
Adding and Deleting Products:

Users can add new products to the product database by providing ID, name, price, and category.
Existing products can be deleted from the database based on their ID.
Data Persistence
The script utilizes a text file (ProductsData.txt) to store product data.
It also employs pickle to save and load the state of the shopping cart, enabling users to resume their shopping session later.
Notes
Ensure that the product ID is unique while adding new products.
Verify the input format when adding products (ID as integer, name and category as string, price as integer or float).
Authors
[Nalla Vinay Reddy]
