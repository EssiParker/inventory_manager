# Create a program that allows you to view, edit, search and report on shoe inventory at a Nike warehouse.

# Create a global variable that is a header that can printed out throughout the program.
header = "\nCountry, Code, Product, Cost, Quantity\n"


# ====== CLASS ======

# Create class Shoe.
class Shoe:

    # Define init method with self and other needed parameters.
    def __init__(self, country, code, product, cost, quantity):
        pass
        # Initialise the attributes to describe a shoe.
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # Create a method to return the quantity of shoes.
    def get_quantity(self):
        pass
        return int(self.quantity)

    # Create a method to return the cost of shoes.
    def get_cost(self):
        pass
        return int(self.cost)

    # Create a method to return a string representation of class.
    def __str__(self):
        pass
        return (f'{self.country} {self.code} {self.product} {self.cost} {self.quantity}')


# Create an empty list that will store list of all shoe objects in the program.
shoes_list = []

#  ======= Define all FUNCTIONS outside the class Shoe =======

# Create the function for the user to read the data from the inventory file, this will be option 1 in the menu.
def read_shoes_data():
    pass
    if len(shoes_list) == 0:

        # Use try-except error handling to open file to read.
        try:
            with open('inventory.txt', 'r+') as inventory:

                # Skip the header line and start the iteration from line below.
                # Use for loop to iterate through the file, append shoe objects to the empty list.
                next(inventory)
                for line in inventory:
                    line = line.strip('\n').split(',')
                    new_shoe = Shoe(line[0], line[1], line[2], int(line[3]), int(line[4]))
                    shoes_list.append(new_shoe)

            print("The data from the inventory has been successfully uploaded to be used by the program.")

        except FileNotFoundError:
            print(f"\nThe file does not exist.")
            quit()

    else:
        print("Shoe data is already loaded, you can view it by entering option '3' in the Menu.")


# Create function for the user to capture data about a shoe, create object and append to shoe list, option 2 in the menu.
def capture_shoes():
    pass
    # Ask the user to enter the details of the shoe they want to add to the inventory.
    print(f"\n====== New Stock ======\n")
    country = input("Enter the country: ")
    code = input("Enter the shoe code: ")
    product = input("Enter the product name: ")
    cost = input("Enter the product cost: ")
    quantity = input("Enter the product quantity: ")

    # Create a new variable for the new shoe information, append to the list.
    new_shoe = Shoe(country, code, product, cost, quantity)
    shoes_list.append(new_shoe)

    # Write the updated list of shoes to the inventory.txt file.
    with open('inventory.txt', 'w+') as inventory:
        inventory.write(f"Country,Code,Product,Cost,Quantity\n")
        for lines in shoes_list:
            lines = str(f"{lines.country},{lines.code},{lines.product},{lines.cost},{lines.quantity}\n")
            inventory.write(lines)

        print(f"\nNew shoe '{new_shoe.product}' was successfully added to the database.")


# Create a function for the user to view all shoes in the inventory, this is option 3 in the menu.
def view_all():
    pass
    # Use for loop to iterate through the shoe list and print each item.
    print(f"\n====== Warehouse Inventory ======{header}")
    for shoes in shoes_list:
        print(shoes)


# Create a function for the user to view shoe with the lowest stock and update it, this is option 4 in the menu.
def re_stock():
    pass
    # Set value for the first object in the list as min_stock.
    min_stock = shoes_list[0]

    # Use for loop to iterate through shoe list to get 'min_stock' by checking if next object quantity if < than current.
    for shoe_stock in shoes_list:
        if shoe_stock.quantity < min_stock.quantity:
            min_stock = shoe_stock

    # Print the lowest stock object.
    print(f"\n====== Low Stock ======{header}"
          f"\n{min_stock}")

    # Ask the user if they want to update the stock.
    add_stock = input("\nEnter Y/N to update the shoes stock: ").lower()

    # Ask the user the quantity and update it.
    if add_stock == "y":
        update_stock = int(input("Please enter quantity for restocking: "))
        min_stock.quantity = int(min_stock.quantity) + update_stock

    else:
        quit()

    # Print the updated stock.
    print(f"\n====== Updated Stock ======{header}"
              f"\n{min_stock}")

    # Write the newly updated shoe list to the inventory.txt file.
    with open('inventory.txt', 'w+') as inventory:
        inventory.write(f"Country,Code,Product,Cost,Quantity\n")
        for lines in shoes_list:
            lines = str(f"{lines.country},{lines.code},{lines.product},{lines.cost},{lines.quantity}\n")
            inventory.write(lines)

        print(f"\nThe stock for'{min_stock.product}' has now been successfully updated in the database.")


# Create a function for the user to search for a particular shoes using shoe code, this is option 5 in the menu.
def search_shoe():
    pass
    # Ask the user to input the product code to search.
    print(f"\n====== Stock Search ======\n")
    shoe_search = input("Please enter the product code to search for shoes in the stock: ")

    # Use for loop to iterate through the shoe list to find the matching item.
    for stock_item in shoes_list:
        if stock_item.code == shoe_search:
            # Print the object.
            print(f"\n====== Results ======{header}"
                  f"\n{stock_item.country} {stock_item.code} {stock_item.product} {stock_item.cost} {stock_item.quantity}")


# Create a function for the user to calculate the value of all items in stock, this will be option 6 in the menu.
def value_per_item():
    pass
    # Print heading before printing all stock information with values.
    print(f"\n====== Stock Values ======"
          f"\nCountry Code Product Cost Quantity \t\t\t Value\n")

    # Use for loop to iterate through the shoe list to calculate the values for all objects.
    for shoe in shoes_list:
        stock_value = int(shoe.cost) * int(shoe.quantity)
        print(f"{shoe.country} {shoe.code} {shoe.product} {shoe.cost} {shoe.quantity} \t\t {stock_value}")


# Create a function to find the shoes with the highest quantity, print this for being on sale, option 7 in the menu.
def highest_qty():
    pass
    # Set the value for the first object in the list as highest_stock.
    highest_stock = shoes_list[0]

    # Use for loop to iterate through shoe list to get 'high_stock' by checking if next object quantity if > than current.
    for shoe_stock in shoes_list:
        if shoe_stock.quantity > highest_stock.quantity:
            highest_stock = shoe_stock

    # Print the highest stock object.
    print(f"\n====== Stock for Sale ======{header}"
          f"\n{highest_stock}")

    # Ask the user to input the discount amount, calculate new price.
    stock_discount_price = int(input("\nPlease enter how much to take off the price: "))
    highest_stock.cost = int(highest_stock.cost) - stock_discount_price

    # Print the update item with new discounted price.
    print(f"\n====== Stock for Sale ======{header}"
          f"\n{highest_stock}")

    # Write the updated list to the inventory.txt file.
    with open('inventory.txt', 'w+') as inventory:
        inventory.write(f"Country,Code,Product,Cost,Quantity\n")
        for lines in shoes_list:
            lines = str(f"{lines.country},{lines.code},{lines.product},{lines.cost},{lines.quantity}\n")
            inventory.write(lines)

        print(f"\nThe database has been updated with the discounted price for {highest_stock.product}.")


# ====== MAIN MENU ======

# Create a program menu with all the options for the user to choose from.
def inventory_manager():
    print("\n======== The Nike Inventory Manager ========\n")

    # Call the function to retrieve the data from the inventory text file that's needed in the program.
    read_shoes_data()

    user_option = ""

    # While the user option is not equal to quit, the menu is presented to them.
    while user_option != 8:

        print(f"\n======= MENU =======")
        # Ask the user to choose the action they would like to perform and call the function.
        user_option = int(input('''\nWhat would you like to do?
        1 - Read stock data from file
        2 - Add new stock item
        3 - View all stock in the inventory list
        4 - View item with the lowest quantity in stock and update it
        5 - Search for a particular stock item
        6 - Calculate the total value for all items in stock
        7 - View stock with the highest stock and reduce the price
        8 - Quit program
        \nEnter number: '''))

        if user_option == 1:
            read_shoes_data()
        elif user_option == 2:
            capture_shoes()
        elif user_option == 3:
            view_all()
        elif user_option == 4:
            re_stock()
        elif user_option == 5:
            search_shoe()
        elif user_option == 6:
            value_per_item()
        elif user_option == 7:
            highest_qty()
        elif user_option == 8:
            print("\nGoodbye!")
            quit()
        else:
            print("\nIncorrect input, please try again.")

# Run the above program.
inventory_manager()
