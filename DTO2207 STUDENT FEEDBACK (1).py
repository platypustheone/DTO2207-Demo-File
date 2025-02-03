BELOW_6000_BASE_RATE = 8.00
ABOVE_100000_BASE_RATE = 15.00
IN_BETWEEN_BASE_RATE = 12.00

BOX_HEIGHT_STRING = "HEIGHT"
BOX_WIDTH_STRING = "WIDTH"
BOX_DEPTH_STRING = "DEPTH"

SOUTH_ISLAND_INCREASE = 1.5
STEWART_ISLAND_INCREASE = 2

def box_dimension(name, dimension):
    """This function asks for the user to input the centimetre length of a specified dimension, which will be rounded to 2 decimal points.
    Due to ONLINZ's specifications, the function does not accept side length values below 5cm or above 100cm. Non-numerical inputs are rejected.
    This function has been added to reduce code repetition.
    """
    while True:
        try:
            side_length = float(input(f"\nHi {name}, please enter the {dimension} of the box, in centimetres, that you will return the product in. All values will be rounded to 2 decimal points.\n>> "))
            if side_length <= 0:
                print("This value is not possible for a side length.\n")
            elif side_length < 5 and side_length > 0:
                print(f"The box's {dimension} must be greater than 5cm.\n")
            elif side_length > 100:
                print(f"The box's {dimension} must be less than 100cm.\n")
            else:
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

# Asks the user for the customer's first name, last name, and home address.
first_name = input("Please enter your first name:\n>> ").title()
last_name = input("\nWhat is your last name?\n>> ").title()
customer_address = input("\nWhat is your home address?\n>> ").title()

# Asks the user for the customer's phone number. Non-integer inputs are rejected.
while True:
    try:
        phone_number = int(input("\nWhat is your personal phone number? This is assuming your phone is based in New Zealand; please omit the leading +64 or zero in that case.\n>> "))
        phone_number_length = len(str(phone_number))
        if phone_number_length >=3 and phone_number_length <= 14:
            break
        else:
            print("\nThis is not a valid input. Please enter a valid phone number.")
    except ValueError:
        print("\nThis is not a valid input. Please enter a valid phone number.")

# Asks the user for the three side lengths of the box using the box_dimension calculation.
box_height = box_dimension(first_name, BOX_HEIGHT_STRING)
box_width = box_dimension(first_name, BOX_WIDTH_STRING)
box_depth = box_dimension(first_name, BOX_DEPTH_STRING)

# Calculates the volume of the customer's box using the box_volume_calculation function.
box_volume = box_volume_calculation(box_height, box_width, box_depth)

# A set of if-else statements determining the base rate of the customer's courier fee.
if box_volume < 6000:
    base_rate = BELOW_6000_BASE_RATE
    print(f"\nYour box's volume is {box_volume:.2f}cm^3. As this is less than 6000cm^3, your base rate is $8.00 NZD.\n")
elif box_volume > 100000:
    base_rate = ABOVE_100000_BASE_RATE
    print(f"\nYour box's volume is {box_volume:.2f}cm^3. As this is greater than 100000cm^3, your base rate is $15.00 NZD.\n")
# If the box volume is between 6000cm^3 and 100000cm^3 (boundary values inclusive).
else:
    base_rate = IN_BETWEEN_BASE_RATE
    print(f"\nYour box's volume is {box_volume:.2f}cm^3. As this is between the values of 6000cm^3 and 100000cm^3 (boundary values inclusive), your base rate is $12.00 NZD.\n")

# Asks the user which New Zealand island they will be sending the box from. This choice will determine their total courier fee. Non-integer inputs are rejected.
while True:
    try:
        return_island = int(input("Please select which island the box will be returned from.\n1 = NORTH ISLAND (TE IKA A MAUI)\n2 = SOUTH ISLAND (TE WAI POUNAMU)\n3 = STEWART ISLAND (RAKIURA)\n>> "))
        nz_island_index = return_island - 1
        if nz_island_index == 0:
            # Keeps the base rate unchanged.
            courier_fee = base_rate
            print(f"\nYou have chosen the {nz_islands[nz_island_index].upper()}. This means that your courier fee is still ${courier_fee:.2f} NZD, as your base rate has stayed the same.")
            break
        elif nz_island_index == 1:
            # Increases base rate by 50%.
            courier_fee = base_rate * SOUTH_ISLAND_INCREASE
            print(f"\nYou have chosen the {nz_islands[nz_island_index].upper()}. This means that your courier fee is now ${courier_fee:.2f} NZD, as your base rate has increased by 50%.")
            break
        elif nz_island_index == 2:
            # Doubles the base rate.
            courier_fee = base_rate * STEWART_ISLAND_INCREASE
            print(f"\nYou have chosen {nz_islands[nz_island_index].upper()}. This means that your courier fee is now ${courier_fee:.2f} NZD, as your base rate has doubled.")
            break
        else:
            print("\nThis is not a valid input. Please select one of the given options.\n")
    except ValueError:
        print("\nThis is not a valid input. Please select one of the given options.\n")

# Adds all of the details to a list containing the customer's details, as is outlined in the specifications.
customer_details.extend([first_name, last_name, customer_address, phone_number, courier_fee])

# Prints the customer's full name, home address, personal number, and the courier fee of their order, as is outlined in the specifications.
print(f"\nYour full name is {customer_details[0]} {customer_details[1]}."
      f"\nYour address is {customer_details[2]}."
      f"\nYour phone number is +64{customer_details[3]}."
      f"\nThe cost of your order is ${customer_details[4]:.2f} NZD.")
