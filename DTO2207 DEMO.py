# A program designed for calculating courier costs.

def box_dimension(name, dimension):
    """This function asks for the user to input the centimetre length of a specified dimension, which will be rounded to 2 decimal points.
    Due to ONLINZ's specifications, the function does not accept side length values below 5cm or above 100cm. Non-numerical inputs are rejected.
    This function has been added to reduce code repetition."""
    while True:
        try:
            while True:
                side_length = float(input("Hi {}, please enter the {} of the box, in centimetres, that you will return the product in. All values will be rounded to 2 decimal points.\n>> ".format(name, dimension)))
                if side_length < 5 and side_length > 0:
                    print("The box's {} must be greater than 5cm.\n".format(dimension))
                elif side_length > 100:
                    print("The box's {} must be less than 100cm.\n".format(dimension))
                elif side_length <= 0:
                    print("This value is not possible for a side length.\n")
                else:
                    break
            break
        except ValueError:
            print("Please enter a number.")

    return side_length

def box_volume_calculation(height, width, depth):
    """This function calculates the volume of the customer's box from the side lengths provided."""
    volume = height*width*depth
    return volume

# A list containing both the customer's details and the cost of their order. Will be updated as the program runs.
customer_details = []

# A list containing the islands of New Zealand. The islands have been placed in list format to allow for updates (e.g., the addition of other relevant locations such as Waikehe Island).
nz_islands = ["North Island", "South Island", "Stewart Island"]

# Asks the user for the customer's first name.
first_name = input("Please enter your first name:\n>> ").title()
customer_details.append(first_name)

# Asks the user for the three side lengths of the box using the box_dimension calculation.
box_height = box_dimension(first_name, "HEIGHT")
box_width = box_dimension(first_name, "WIDTH")
box_depth = box_dimension(first_name, "DEPTH")

# Calculates the volume of the customer's box using the box_volume_calculation function.
box_volume = box_volume_calculation(box_height, box_width, box_depth)

# A set of if-else statements determining the base rate of the customer's courier fee.
if box_volume < 6000:
    base_rate = 8.00
    print("Your box's volume is {:.2f}cm^3. As this is less than 6000cm^3, your base rate is $8.00 NZD.\n".format(box_volume))
elif box_volume >= 6000 and box_volume <= 100000:
    base_rate = 12.00
    print("Your box's volume is {:.2f}cm^3. As this is between the values of 6000cm^3 and 100000cm^3 (boundary values inclusive), your base raate is $12.00 NZD.\n".format(box_volume))
# If their box's volume is above 100000cm^3.
else:
    base_rate = 15.00
    print("Your box's volume is {:.2f}cm^3. As this is greater than 100000cm^3, your base rate is $15.00 NZD.\n".format(box_volume))

# Asks the user which New Zealand island they will be sending the box from. This choice will determine their total courier fee.
while True:
    return_island = input("Please select which island the box will be returned from.\n1 = NORTH ISLAND (TE IKA A MAUI)\n2 = SOUTH ISLAND (TE WAI POUNAMU)\n3 = STEWART ISLAND (RAKIURA)\n>> ")
    if return_island == "1":
        courier_fee = base_rate
        print("\nYou have chosen the NORTH ISLAND. This means that your courier fee is now ${:.2f} NZD, as your base rate has stayed the same.".format(courier_fee))
        break
    elif return_island == "2":
        # Increases base rate by 50%.
        courier_fee = base_rate * 1.5
        print("\nYou have chosen the SOUTH ISLAND. This means that your courier fee is now ${:.2f} NZD, as your base rate has increased by 50%.".format(courier_fee))
        break
    elif return_island == "3":
        courier_fee = base_rate * 2
        print("\nYou have chosen STEWART ISLAND. This means that your courier fee is now ${:.2f} NZD, as your base rate has doubled.".format(courier_fee))
        break
    else:
        print("\nThis is not a valid input. Please select one of the given options.\n")

# Asks the user for their last name, their home address, and their personal phone number.
last_name = input("\nWhat is your last name?\n>> ").capitalize()
customer_address = input("\nWhat is your address?\n>> ").title()
phone_number = input("\nWhat is your phone number?\n>> ")

# Adds all of the details to a list containing the customer's details, as is outlined in the specifications.
customer_details.extend([last_name, customer_address, phone_number, courier_fee])

# Prints the customer's full name, home address, personal number, and the courier fee of their order, as is outlined in the specifications.
print("Your full name is {} {}.".format(first_name, last_name))
print("Your address is {}.".format(customer_address))
print("Your phone number is {}.".format(phone_number))
print("The cost of your order is ${:.2f} NZD.".format(courier_fee))
