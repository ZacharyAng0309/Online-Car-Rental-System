# Code by Ang Zi Yang Adrian Lee Song Yue
#         TP059610    TP060648

# import
import datetime
import os

# Clear terminal
def clear():
    os.system("cls")


# data_validation functions
def get_int(message):
    while True:
        try:
            input_int = int(input(message))
            if input_int < 0:
                print("Please enter a positive number.")
                print("=" * 210)
            else:
                return input_int
        except ValueError:
            print("Please enter a number only.")


def get_float(message):
    while True:
        try:
            input_int = float(input(message))
            if input_int < 0:
                print("Please enter a positive number.")
                print("=" * 210)
            else:
                return input_int
        except ValueError:
            print("Please enter a number only.")


def input_validation(message):
    while True:
        try:
            raw_input = input(message)
            input_int = int(raw_input)
            if input_int < 0:
                print("Please enter a positive number.")
            else:
                return input_int
        except:
            return raw_input


def get_rentals():
    rental_list = []
    with open("rental_list.txt", "r") as rf:
        for lines in rf:
            rental_records = lines.rstrip("\n").split("/")
            if len(rental_records) > 1:
                rental_list.append(rental_records)
            else:
                continue
    return rental_list


def get_cars():
    car_list = []
    with open("car_list.txt", "r") as rf:
        for lines in rf:
            car_records = lines.rstrip("\n").split("/")
            if len(car_records) > 1:
                car_list.append(car_records)
            else: 
                continue
    return car_list


def validating_password(message):
    while True:
        password = input(message)
        if len(password) > 4:
            if len(password) < 11:
                print("Password accepted.")
                return password
            else:
                print("Enter a password with less than 10 characters.")
        else:
            print("Enter a password with at least 5 character.")


def validating_identification(message):
    while True:
        input_ic = input(message)
        if (
            input_ic[:6].isdigit()
            and input_ic[7:9].isdigit()
            and input_ic[10:].isdigit()
            and input_ic[6] == "-"
            and input_ic[9] == "-"
            and len(input_ic) == 14
        ):
            return input_ic
        else:
            print("Please enter a valid IC.")


def validating_phone(message):
    while True:
        input_pn = input(message)
        if input_pn[:3].isdigit() and input_pn[4:].isdigit() and input_pn[3] == "-":
            return input_pn
        else:
            print("Please enter a valid Phone Number.")


def validating_date(message):
    while True:
        try:
            date = input(message)
            date = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
            return date
        except:
            print("Please enter a valid date or correct format.")


def validating_payment_method():
    payment_list = ["Cash", "Credit card", "Online banking"]
    while True:
        payment_method = input(
            "Please choose a payment method (Cash/Credit card/Online banking): "
        ).capitalize()
        if payment_method in payment_list:
            return payment_method
        else:
            print("Please enter a valid payment method.")


# Functional functions
def list_to_string(list):
    list_length = len(list)
    text = ""
    for i in range(list_length):
        if int(i) != list_length - 1:
            text += list[i] + "/"
        else:
            text += list[i]
    return text


def display_list(list, num):
    text = ""
    for i in list:
        text += i + " " * (num - len(i)) + "|"
    return text


# General Features
def registration():
    is_valid = False
    while not is_valid:
        #Getting username
        existed_username = []
        with open("user_list.txt", "r") as rf:
            column_name = rf.readline().rstrip("\n").split("/")
            for records in rf:
                existed_username.append(records.rstrip("\n").split("/")[0])
        new_user = []
        # Menu Interface
        print("=" * 210)
        print("Registration".center(210))
        print("=" * 210)
        print("(Note : You are not allowed to change the username afterwards, Enter 'exit' to quit registration.)")
        # Validating username
        is_username = True
        username = input("Enter a username : ")
        if (
            username == " "
            or username.capitalize() == "Username"
            or username.lower() == "admin"
        ):
            is_username = False
        elif username.lower() == "exit":
            clear()
            return
        else:
            for usernames in existed_username:
                if username == usernames:
                    is_username = False
                else:
                    continue
        if is_username:
            is_valid = True
            print("Username Accepted.")
            new_user.append(username)
        else:
            print("=" * 210)
            print("This username is not available.")
            confirmation = ""
            while not confirmation == "y" and not confirmation == "n":
                confirmation = input("Do you wish to try again?(y/n): ").lower()
                if confirmation == "y":
                    clear()
                    pass
                elif confirmation == "n":
                    clear()
                    return
                else:
                    print("Invalid input. Please enter y for YES or and for NO.")
    # Validating password
    print("=" * 210)
    password = validating_password("Please enter your password: ")
    new_user.append(password)
    # Getting user details
    print("=" * 210)
    print("Kindly please provide your personal details.")
    for index in range(2, len(column_name)):
        if index == 3:
            user_details = validating_identification(
                "Enter your detail for IC (xxxxxx-xx-xxxx): "
            )
            new_user.append(user_details)
        elif index == 4:
            user_details = validating_phone(
                "Enter your detail for Phone Number (xxx-xxxxxxx): "
            )
            new_user.append(user_details)
        else:
            user_details = input(f"Enter your detail for {column_name[index]}: ")
            new_user.append(user_details)
    # Registering new user
    with open("user_list.txt", "a") as f:
        f.write(list_to_string(new_user) + "\n")
    clear()
    print("=" * 210)
    print(
        "Account Registered. Please log in to get access to more functionalities."
    )
    return

def login():
    is_login = False
    while not is_login:
        # initialization for admin account
        admin_ID = "admin"
        admin_password = "admin"
        # Menu Interface
        print("=" * 210)
        print("Login Menu".center(210))
        print("=" * 210)
        print("(Note: Enter 'exit' to quit login menu.)")
        # Getting username & password
        username = input("Enter your Username: ")
        if username.lower() == "exit":
            clear()
            return
        password = input("Enter your Password: ")
        if username.capitalize() == "Username":
            pass
        else:
            # Login for Admin
            if username == admin_ID:
                if password == admin_password:
                    is_login = True
                    clear()
                    print("Login Successfully. Welcome back, Administrator.")
                    admin_menu()
                    return
                else:
                    pass
            # Login for user
            else:
                with open("user_list.txt", "r") as rf:
                    for lines in rf:
                        userdata = lines.strip().split("/")
                        if username == userdata[0] and password == userdata[1]:
                            clear()
                            print(f"Welcome back, {username}!")
                            is_login = True
                            registered_user_menu(username)
                            return
                        else:
                            continue
        # Invalid Login
        if is_login == False:
            print("=" * 210)
            print("Invalid password or account not existed.")
            confirmation = ""
            while not confirmation == "y" and not confirmation == "n":
                confirmation = input("Do you want to retry?(y/n): ").lower()
                if confirmation == "y":
                    clear()
                    pass
                elif confirmation == "n":
                    clear()
                    print("You will be redirected back to the home page....")
                    return
                else:
                    print("Invalid input. Please enter y for YES or n for NO.")

def view_available_cars():
    # Getting car list
    car_list = get_cars()
    column_name = car_list[0]
    #Menu Interface
    print("=" * 210)
    print("Available Car List".center(210))
    print("=" * 210)
    print(display_list(column_name[:6], 20))
    print("-" * 126)
    #Filtering cars available for rent
    is_displayed = False
    for records in car_list:
        if records[6] != "Unavailable" and records[6] != "Status":
            is_displayed = True
            print(display_list(records[:6], 20))
        else:
            continue
    if not is_displayed:
        print("(No record found.)")
    confirmation = ""
    while not confirmation == "y":
        print("=" * 210)
        confirmation = input("Enter y to exit to menu: ").lower()
        if confirmation == "y":
            clear()
            return
        else:
            print("Enter y only.")

# Admin Features
def view_users():
    #Getting User
    user_list = []
    with open("user_list.txt", "r") as rf:
        for records in rf:
            user = records.rstrip("\n").split("/")
            if len(user) > 1:
                temp = []
                for i in range(len(user)):
                    #Filtering User Password
                    if i == 0 or i > 1:
                        temp.append(user[i])
                user_list.append(temp)
            else:
                continue
    #Menu Interface
    print("=" * 210)
    print("User List".center(210))
    print("=" * 210)
    is_displayed = False
    print(display_list(user_list[0], 20))
    print("-" * 105)
    #Display User Details
    for i in range(1, len(user_list)):
        if user_list[i] == " ":
            pass
        else:
            is_displayed = True
            print(display_list(user_list[i], 20))
    if not is_displayed:
        print("(No record found.)")
    confirmation = ""
    while not confirmation == "y":
        print("=" * 210)
        confirmation = input("Enter y to exit to menu: ").lower()
        if confirmation == "y":
            clear()
            return
        else:
            print("Please Enter y only.")

def view_available_cars_for_admin():
    # Getting car list
    car_list = get_cars()
    column_name = car_list[0]
    #Menu Interface
    print("=" * 210)
    print("Car List".center(210))
    print("=" * 210)
    print(display_list(column_name, 20))
    print("-" * 147)
    #Filtering & Displaying Currently Available Car
    is_displayed = False
    for records in car_list:
        if records[6] =="Available":
            is_displayed = True
            print(display_list(records, 20))
        else:
            continue
    if not is_displayed:
        print("(No record found.)")
    confirmation = ""
    while not confirmation == "y":
        print("=" * 210)
        confirmation = input("Enter y to exit to menu: ").lower()
        if confirmation == "y":
            clear()
            return
        else:
            print("Enter y only.")

def view_rented_cars():
    # Getting car list
    car_list = get_cars()
    # Menu Interface
    print("=" * 210)
    print("Rented Car List".center(210))
    print("=" * 210)
    print(display_list(car_list[0], 20))
    print("-" * 147)
    is_displayed = False
    # Filtering & Displaying Rented Cars
    for records in car_list:
        if records[6] == "Rented":
            print(display_list(records, 20))
            is_displayed = True
        else:
            continue
    if not is_displayed:
        print("(No record found.)")
    confirmation = ""
    while not confirmation == "y":
        print("=" * 210)
        confirmation = input("Enter y to exit to menu: ").lower()
        if confirmation == "y":
            clear()
            return
        else:
            print("Please Enter y only.")

def view_customer_bookings():
    while True:
        # Getting bookings
        booking_list = get_rentals()
        general_booking_list = []
        for records in booking_list:
            if records[6] == "Pending" and records[7] == "False":
                general_booking_list.append(records[:-2])
            else:
                continue
        # Menu Interface
        column_name = booking_list[0]
        print("=" * 210)
        print("View Customer Booking".center(210))
        print("=" * 210)
        print("Option 1 : General Booking List")
        print("Option 2 : Bookings of specific user")
        print("(Note: Please enter 'exit' to quit to menu.)")
        print("=" * 210)
        # Getting option
        is_valid = False
        while not is_valid:
            option = input_validation("Enter an option: Option ")
            #exit
            if type(option) == str:
                if option == "exit":
                    clear()
                    return
                else:
                    print("Please enter a number.")
            else:
                #Display All Bookings
                if option == 1:
                    # Menu Interface
                    is_valid = True
                    clear()
                    print("=" * 210)
                    print("Booking List".center(210))
                    print("=" * 210)
                    print(display_list(column_name[:-2], 20))
                    print("-" * 168)
                    if len(general_booking_list) == 0:
                        print("(No records found.)")
                        confirmation = ""
                        while not confirmation == "y":
                            print("=" * 210)
                            confirmation = input("Enter y to exit to menu: ").lower()
                            if confirmation == "y":
                                clear()
                                return
                            else:
                                print("Please Enter y only.")
                    else:
                        for i in general_booking_list:
                            print(display_list(i, 20))
                #Filter & Display bookings from a specific user
                elif option == 2:
                    is_valid = True
                    is_displayed = False
                    while not is_displayed:
                        username = input(
                            "Please enter the username of the customer to search for his/her records: "
                        )
                        # Getting user bookings
                        user_booking_list = []
                        for records in general_booking_list:
                            if records[1] == username:
                                user_booking_list.append(records)
                        # Menu Interface
                        clear()
                        print("=" * 210)
                        print("Booking List".center(210))
                        print("=" * 210)
                        print(display_list(column_name[:-2], 20))
                        print("-" * 168)
                        #Displaying bookings from the user
                        if len(user_booking_list) == 0:
                            print("(No records found for this customer.)")
                            confirmation = ""
                            while not confirmation == "y" and not confirmation == "n":
                                print("=" * 210)
                                confirmation = input(
                                    "Do you wish to try again?(y/n): "
                                ).lower()
                                if confirmation == "y":
                                    pass
                                elif confirmation == "n":
                                    is_displayed = True
                                else:
                                    print(
                                        "Invalid input. Please enter y for YES or n for NO."
                                    )
                        else:
                            is_displayed = True
                            for i in user_booking_list:
                                print(display_list(i, 20))
                #Error message
                else:
                    print("Please enter an option within the given range.")

        if is_valid:
            confirmation = ""
            while not confirmation == "y" and not confirmation == "n":
                print("=" * 210)
                confirmation = input(
                    "Do you wish to continue viewing booking list?(y/n): "
                ).lower()
                if confirmation == "y":
                    clear()
                    pass
                elif confirmation == "n":
                    clear()
                    return
                else:
                    print("Invalid input. Please enter y for YES or n for NO.")


def view_customer_payments():
    while True:
        # Getting bookings
        rental_list = get_rentals()
        # Getting payment columns
        column_name = rental_list[0]
        payment_column = []
        for i in range(len(column_name)):
            if i < 2 or i == 5 or i > 6:
                payment_column.append(column_name[i])
            else:
                continue
        # Getting payment
        payment_record = []
        for records in rental_list:
            if records[7] == "Paid":
                temp = []
                for index in range(len(records)):
                    if index < 2 or index == 5 or index > 6:
                        temp.append(records[index])
                    else:
                        continue
                payment_record.append(temp)
        # Menu Interface
        print("=" * 210)
        print("View Customer Booking".center(210))
        print("=" * 210)
        print("Option 1 : Payments within specific date/time")
        print("Option 2 : Payments from a specific user")
        print("(Note: Please enter 'exit' to quit to menu.)")
        print("=" * 210)

        is_valid = False
        while not is_valid:
            option = input_validation("Enter an option: Option ")
            #exit
            if type(option) == str:
                if option == "exit":
                    clear()
                    return
                else:
                    print("Please enter a number.")
            else:
                # Payments within a specific time range
                if option == 1:
                    is_valid = True
                    # Menu Interface
                    print("=" * 210)
                    print("Filter".center(210))
                    print("=" * 210)
                    # Validating starting time & ending time
                    start_time = validating_date("Please enter the starting time of the selected range. (yyyy-mm-dd hh:mm:ss): ")
                    end_time = validating_date("Please enter the ending time of the selected range.   (yyyy-mm-dd hh:mm:ss): ")
                    clear()
                    # Menu Interface
                    print("=" * 210)
                    print("Payment List".center(210))
                    print("=" * 210)
                    print(display_list(payment_column, 20))
                    print("-" * 126)
                    #Displaying payments
                    general_payment_list = []
                    for records in payment_record:
                        record_time = datetime.datetime.strptime(
                            records[5], "%Y-%m-%d %H:%M:%S"
                        )
                        if record_time > start_time and record_time < end_time:
                            general_payment_list.append(records)
                    if len(general_payment_list) == 0:
                        print("(No record found.)")
                    else:
                        for i in general_payment_list:
                            print(display_list(i, 20))
                #Payments from a specific customer
                elif option == 2:
                    is_valid = True
                    is_displayed = False
                    while not is_displayed:
                        username = input(
                            "Please enter the username of the customer to search for his/her records: "
                        )
                        # Getting user bookings
                        user_payment_list = []
                        for records in payment_record:
                            if records[1] == username:
                                user_payment_list.append(records)
                        # Menu Interface
                        clear()
                        print("=" * 210)
                        print("Booking List".center(210))
                        print("=" * 210)
                        print(display_list(payment_column, 20))
                        print("-" * 126)
                        #Displaying Payments from the user
                        if len(user_payment_list) == 0:
                            print("(No records found for this customer.)")
                            confirmation = ""
                            while not confirmation == "y" and not confirmation == "n":
                                print("=" * 210)
                                confirmation = input(
                                    "Do you wish to try again?(y/n): "
                                ).lower()
                                if confirmation == "y":
                                    pass
                                elif confirmation == "n":
                                    is_displayed = True
                                else:
                                    print(
                                        "Invalid input. Please enter y for YES or n for NO."
                                    )
                        else:
                            is_displayed = True
                            for i in user_payment_list:
                                print(display_list(i, 20))
                else:
                    print("Please enter an option within the given range.")
        if is_valid:
            confirmation = ""
            while not confirmation == "y" and not confirmation == "n":
                print("=" * 210)
                confirmation = input(
                    "Do you wish to continue viewing payment list?(y/n): "
                ).lower()
                if confirmation == "y":
                    clear()
                    pass
                elif confirmation == "n":
                    clear()
                    return
                else:
                    print("Invalid input. Please enter y for YES or n for NO.")


def add_car():
    while True:
        # Getting car list
        car_list = get_cars()
        # Getting new CarID
        new_car = []
        new_carID = len(car_list)
        new_car.append(f"C{new_carID:03}")
        # Menu interface
        column_name = car_list[0]
        print("=" * 210)
        print("New Car Form".center(210))
        print("=" * 210)
        print(f"New car (carID : C{new_carID:03}) is created.")
        confirmation = ""
        while not confirmation == "y" and not confirmation == "n":
            confirmation = input("Do you want to continue operation?(y/n): ").lower()
            if confirmation == "y":
                clear()
                pass
            elif confirmation == "n":
                clear()
                return
            else:
                print("Invalid input. Please enter y for YES or n for NO.")
        # Menu Interface
        print("=" * 210)
        print("New Car Details".center(210))
        print("=" * 210)
        print(f"CarID : C{new_carID:03}")
        # Adding car details
        for i in range(1, len(column_name)):
            if i == 4:
                car_detail = get_int(f"Enter your detail for {column_name[i]}: ")
                new_car.append(str(car_detail))
            elif i == 5:
                car_detail = get_float(f"Enter your detail for {column_name[i]}: ")
                new_car.append(str(car_detail))
            elif i == 6:
                is_valid = False
                car_status = ["Available", "Rented", "Unavailable"]
                while not is_valid:
                    car_detail = input(
                        f"Enter your detail for {column_name[i]} (Available/Rented/Unavailable): "
                    ).capitalize()
                    if car_detail in car_status:
                        is_valid = True
                        new_car.append(car_detail)
                    else:
                        print(
                            f"Only 'Rented' or 'Available' or 'Unavailable' is available for {column_name[i]}."
                        )
            else:
                new_car.append(input(f"Enter The detail for {column_name[i]}: "))
        # Updating file
        with open("car_list.txt", "a") as f:
            f.write(list_to_string(new_car) + "\n")
        print("=" * 210)
        print(f"New Car with carID({new_carID:03}) is added.")
        confirmation = ""
        while not confirmation == "y" and not confirmation == "n":
            confirmation = input("Do you wish to add more cars?(y/n): ").lower()
            if confirmation == "y":
                clear()
                pass
            elif confirmation == "n":
                clear()
                return
            else:
                print("Invalid input. Please enter y for YES or n for NO.")


def update_rental_status():
    while True:
        # Getting rental list
        rental_list = get_rentals()
        # Getting rental detail
        rental_records = []
        for record in rental_list:
            if record[7] == "Paid" and record[6] != "Returned":
                temp = []
                for index in range(len(record)):
                    if index < 5 or index == 6:
                        temp.append(record[index])
                    else:
                        continue
                rental_records.append(temp)
        if len(rental_records) == 0:
            print("There is no rental that can be updated.")
            print("You will be directed to the menu...")
            return
        else:
            pass
        # Menu Interface
        column_name = rental_list[0]
        rental_column = []
        for i in range(len(column_name)):
            if i < 5 or i == 6:
                rental_column.append(column_name[i])
        print("=" * 210)
        print("Rental List".center(210))
        print("=" * 210)
        print("Option |", display_list(rental_column, 20))
        print("-" * 135)
        #Displaying rental
        for i in range(len(rental_records)):
            print(
                i + 1, " " * (5 - len(str(i))), ":", display_list(rental_records[i], 20)
            )
        print("(Note: Please enter 'exit' to quit to the menu.)")
        # Validating rental
        is_updated = False
        while not is_updated:
            print("=" * 210)
            option = input_validation(
                "Please enter the option of the rental that you want to update: Option "
            )
            if type(option) == str:
                if option.lower() == "exit":
                    clear()
                    return
                else:
                    print("Please enter a number.")
            else:
                if option - 1 < len(rental_records) and option != 0:
                    is_updated = True
                    outdated_rental = rental_records[option - 1]
                    for record in rental_list:
                        if record[0] == outdated_rental[0]:
                            selected_rental = record
                else:
                    print("Please enter an option within the given range.")
        # Updating Rental Status
        if is_updated:
            is_valid = False
            while not is_valid:
                status = ["Cancelled", "Pending", "Renting", "Returned"]
                updated_status = input(
                    f"Enter the updated rental status for Rental({selected_rental[0]}) (Cancelled/Returned/Pending/Renting): "
                ).capitalize()
                if updated_status in status:
                    is_valid = True
                    #Cancelling a rental
                    if updated_status == "Cancelled":
                        selected_rental[6] = updated_status
                        selected_rental[7] = "False"
                        selected_rental[8] = "False"
                        selected_rental[9] = "False"
                    #Renting & Returning a car
                    elif updated_status == "Returned" or updated_status == "Renting":
                        selected_rental[6] = updated_status
                        car_list = get_cars()
                        if updated_status == "Returned":
                            for record in car_list:
                                if record[0] == selected_rental[2]:
                                    record[6] = "Available"
                        elif updated_status == "Renting":
                                for record in car_list:
                                    if record[0] == selected_rental[2]:
                                        record[6] = "Rented"
                        with open("car_list.txt", "w") as f:
                            for record in car_list:
                                f.write(list_to_string(record) + "\n")
                    else:
                        selected_rental[6] = updated_status
                else:
                    print("Please enter a valid status for the rental.")
            print("=" * 210)
            #Updating rental
            with open("rental_list.txt", "w") as wf:
                for records in rental_list:
                    wf.write(list_to_string(records) + "\n")
            print(f"Rental status for Rental({selected_rental[0]}) is updated.")
            confirmation = ""
            while not confirmation == "y" and not confirmation == "n":
                confirmation = input("Do you wish to continue updating?(y/n): ").lower()
                if confirmation == "y":
                    clear()
                    pass
                elif confirmation == "n":
                    clear()
                    return
                else:
                    print("Invalid input. Please enter y for YES or n for NO.")


def modify_car_detail():
    while True:
        # Getting car list
        car_list = get_cars()
        # Menu Interface
        column_name = car_list[0]
        print("=" * 210)
        print("Car list".center(210))
        print("=" * 210)
        print("Option |", display_list(column_name, 20))
        print("-" * 156)
        for records_index in range(1, len(car_list)):
            print(records_index," " * (5 - len(str(records_index))),":",display_list(car_list[records_index], 20))
        print("(Note: Enter 'exit' to exit to menu.)")
        # Validating car
        is_car = False
        while not is_car:
            print("=" * 210)
            index = input_validation("Enter the Option of the targeted car you wanted to modify: Option ")
            #exit
            if type(index) == str:
                if index.lower() == "exit":
                    clear()
                    return
                else:
                    print("Please enter a number.")
            else:
                #Selecting Car
                if index < len(car_list):
                    if index == 0:
                        print("You are not allowed to modify column name.")
                    else:
                        is_car = True
                        target_car_index = index
                        clear()
                else:
                    print(
                        "Invalid option. Please enter an option within the range given."
                    )
        # Getting Selected Car
        car_details = car_list[target_car_index]
        print("=" * 210)
        print(f"Car Details for Car({car_details[0]})".center(210))
        print("=" * 210)
        for index in range(1, len(car_details)):
            print(f"Option {index}: ({column_name[index]} : {car_details[index]})")
        print("(Note: Enter 'exit' to exit to menu.)")
        # Validating Detail
        is_detail = False
        while not is_detail:
            print("=" * 210)
            option = input_validation("Enter the option you want to modify: Option ")
            if type(option) == str:
                if option.lower() == "exit":
                    clear()
                    return
                else:
                    print("Please enter a number.")
            else:
                if option < len(car_details):
                    # Modifying detail
                    if option == 0:
                        print(f"{car_details[option]} cannot be modified.")
                    else:
                        is_detail = True
                else:
                    print(
                        "Invalid option. Please enter an option within the range given."
                    )
        # Updating car detail
        if is_detail:
            print("=" * 210)
            if option == 4:
                updated_detail = get_int(
                    f"Enter your updated detail for {column_name[option]}: "
                )
                car_details[option] = str(updated_detail)
            elif option == 5:
                updated_detail = get_float(
                    f"Enter your updated detail for {column_name[option]}: "
                )
                car_details[option] = str(updated_detail)
            elif option == 6:
                is_valid = False
                car_status = ["Available", "Rented", "Unavailable"]
                while not is_valid:
                    updated_detail = input(
                        f"Enter your updated detail for {column_name[option]} (Available/Rented/Unavailable): "
                    ).capitalize()
                    if updated_detail in car_status:
                        is_valid = True
                        car_details[option] = updated_detail
                    else:
                        print(
                            f"Only 'Rented' or 'Available' or 'Unavailable' is available for {column_name[option]}."
                        )
            else:
                car_details[option] = input(
                    f"Enter your updated detail for {column_name[option]}: "
                )
            # Updating file
            with open("car_list.txt", "w") as wf:
                for i in car_list:
                    wf.write(list_to_string(i) + "\n")
            print(
                f"Modification for {column_name[option]} of Car {car_details[0]} is successful."
            )
            confirmation = ""
            while not confirmation == "y" and not confirmation == "n":
                print("=" * 210)
                confirmation = input(
                    "Do you wish to continue modifying?(y/n): "
                ).lower()
                if confirmation == "y":
                    clear()
                    pass
                elif confirmation == "n":
                    clear()
                    return
                else:
                    print("Invalid input. Please enter y for YES or n for NO.")


def outdated_booking_cancellation():
    #Initialization
    cancellation = False
    #Getting bookings
    booking_list = get_rentals()
    column_name = booking_list[0]
    #Menu Interface
    print("=" * 210)
    print("Booking List".center(210))
    print("=" * 210)
    print(display_list(column_name, 19))
    print("-" * 200)
    #Filtering outdated bookings
    outdated_bookingID = []
    for records in booking_list:
        try:
            pickup_time = datetime.datetime.strptime(records[3], "%Y-%m-%d %H:%M:%S")
        except:
            continue
        now = datetime.datetime.now().replace(microsecond=0)
        if (records[6] == "Pending"and records[7] == "False"and now > pickup_time):
            outdated_bookingID.append(records[0])
            print(display_list(records, 19))
    if len(outdated_bookingID) == 0:
        print("(No outdated booking found.)")
        confirmation = ""
        while not confirmation == "y":
            print("=" * 210)
            confirmation = input("Enter y to exit to menu: ").lower()
            if confirmation == "y":
                clear()
                return
            else:
                print("Please Enter y only.")
    print("(Note: Enter 'exit' to quit to menu.)")
    #Cancelling outdated bookings
    while cancellation == False:
        print("=" * 210)
        option = input("Please enter 'cancel' to cancel all the outdated bookings: ").lower()
        if option == "exit":
            clear()
            return
        elif option == "cancel":
            cancellation = True
            for record in booking_list:
                if record[0] in outdated_bookingID:
                    record[6] = "Cancelled"
        else:
            print("Please enter 'cancel' or 'exit' only.")
        #Updating booking status
        if cancellation:
            with open("rental_list.txt", "w") as wf:
                for i in range(len(booking_list)):
                    wf.write(list_to_string(booking_list[i]) + "\n")
            clear()
            print("=" * 210)
            print(display_list(column_name[:-3], 19))
            print("-" * 140)
            for record in booking_list:
                if record[0] in outdated_bookingID:
                    print(display_list(record[:-3], 19))
            print("=" * 210)
            print(
                f"Booking({','.join(outdated_bookingID)}) is cancelled successfully."
            )
            print("You will be directed back to the menu...")
            return

# Registered customer Features
def modify_detail(username):
    while True:
        clear()
        #Initialization
        is_modify = False
        loop_count = 0
        customer_list = []
        #Menu Interface
        print("=" * 210)
        print("Modify Details".center(210))
        print("=" * 210)
        #Getting customers
        with open("user_list.txt", "r") as f:
            for lines in f:
                customer_records = lines.rstrip("\n").split("/")
                customer_list.append(customer_records)
        #Getting customer index
        for lines in customer_list:
            if lines[0] == username:
                user_index = loop_count
            else:
                loop_count += 1
                continue
        #Selecting customer
        user_data = customer_list[user_index]
        #Displaying Detail
        headers = customer_list[0]
        for i in range(1, len(headers)):
            print(f"Option {i}: {headers[i]} - {user_data[i]}")
        print("(Note: Enter 'exit' to quit to menu.)")
        print("=" * 210)
        #Selecting Detail
        while is_modify == False:
            input1 = input_validation("Please select an option to modify: Option ")
            #exit
            if type(input1) == str:
                if input1 == "exit":
                    clear()
                    return
                else:
                    print("Please enter a number.")
            else:
                #Modifying Detail
                if input1 < len(user_data):
                    is_modify = True
                    if input1 == 1:
                        user_data[input1] = validating_password(f"Please enter your modified detail for {headers[input1]}: ")
                    elif input1 == 3:
                        user_data[input1] = validating_identification(f"Please enter your modified detail for {headers[input1]}: ")
                    elif input1 == 4:
                        user_data[input1] = validating_phone(f"Please enter your modified detail for {headers[input1]}: ")
                    else:
                        user_data[input1] = input(f"Please enter your modified detail for {headers[input1]}: ")
                #Error Message
                else:
                    print("Please enter the number between 1 - 5.")

        #Updating detail
        if is_modify:
            print("=" * 210)
            print(f"Successfully modified your {headers[input1]} to {user_data[input1]}.")
            with open("user_list.txt", "w") as wf:
                for i in range(len(customer_list)):
                    wf.write(list_to_string(customer_list[i]) + "\n")
            confirmation = ""
            while not confirmation == "y" and not confirmation == "n":
                print("=" * 210)
                confirmation = input(
                    "Do you wish to continue modifying?(y/n): "
                ).lower()
                if confirmation == "y":
                    pass
                elif confirmation == "n":
                    clear()
                    return
                else:
                    print("Invalid input. Please enter y for YES or n for NO.")


def rental_history(username):
    #Initialization
    clear()
    rental_exist = False
    history_list = get_rentals()
    #Menu Interface
    print("=" * 210)
    print("Rental History".center(210))
    print("=" * 210)
    #Getting rental history of the customer
    rent_his = []
    for lines in history_list:
        if lines[1] == username and lines[7] == "Paid":
            rent_his.append(lines)
            rental_exist = True
    #Displaying Rental History
    if rental_exist == False:
        print("(Record not found.)")
    else:
        print(display_list(history_list[0], 19))
        print("-" * 200)
        for i in rent_his:
            print(display_list(i, 19))
    print("=" * 210)
    confirmation = ""
    while not confirmation == "y":
        print("=" * 210)
        confirmation = input("Enter y to exit to menu: ").lower()
        if confirmation == "y":
            clear()
            print("You will be redirected back to User Menu page....")
            return
        else:
            print("Please Enter y only.")

def booking(username):
        #Initialization
        clear()
        is_view = False
        #Menu Interface
        print("=" * 210)
        print("Booking Menu".center(210))
        print("=" * 210)
        #Viewing cars
        while not is_view:
            option = input("Do you want to see the cars for renting?(y/n): ")
            if option == "y":
                is_view = True
                print("You will be directed to Available Car List....")
                car_list = get_cars()
                print("=" * 210)
                print("Available Car List".center(210))
                print("=" * 210)
                print(display_list(car_list[0][:6], 20))
                print("-" * 126)
                for i in range(len(car_list)):
                    if i == 0:
                        continue
                    elif car_list[i][6] != "Unavailable":
                        print(display_list(car_list[i][:6], 20))
                booking_details(username)
                return
            elif option == "n":
                is_view = True
                booking_details(username)
                return
            else:
                print("invalid word. Please enter y for YES or n for NO.")


def booking_details(username):
    while True:
        #initialization
        booking_exist = False
        car_list = get_cars()
        #Creating Booking
        while booking_exist == False:
            print("=" * 210)
            print("(Note: Enter 'exit' to quit to menu.)")
            user_car = input("Please enter the ID of the car you would like to book: ")
            #Exit
            if user_car.lower() == "exit":
                clear()
                return
            else:
                #Validating Car
                rented_hours = []
                for elements in car_list:
                    if user_car == elements[0]:
                        booking_exist = True
                        price_per_hour = float(elements[5])
            #Error Message
            if booking_exist == False:
                print("Car not found. Please try again.")
                confirmation = ""
                while not confirmation == "y" and not confirmation == "n":
                    print("=" * 210)
                    confirmation = input("Do you wish to try again?(y/n): ").lower()
                    if confirmation == "y":
                        pass
                    elif confirmation == "n":
                        clear()
                        return
                    else:
                        print("Invalid input. Please enter y for YES or n for NO.")
        #Getting booked time range of the selected car
        rental_list = get_rentals()
        for record in rental_list:
            if record[2] == user_car and record[6] != "Cancelled":
                rented_hours.append([record[3],record[4]])
        print("=" * 210)
        #Input Pickup Date
        while True:
            pickup_date = validating_date("Please enter pickup time (yyyy-mm-dd hh:mm:ss): ")
            now = datetime.datetime.now().replace(microsecond=0)
            if pickup_date < now:
                print("You are not allowed to select this date.")
            else:
                break
        #Validating time slot for booking
        is_available = True
        for record in rented_hours:
            start_time = datetime.datetime.strptime(record[0], "%Y-%m-%d %H:%M:%S")
            return_time = datetime.datetime.strptime(record[1], "%Y-%m-%d %H:%M:%S")
            if start_time <= pickup_date and pickup_date <= return_time:
                is_available = False
            else:
                continue
        #Generating Booking
        if is_available:
            rent_hour = get_int("Please enter the renting duration (write a number based on hour): ")
            return_date = pickup_date + datetime.timedelta(hours=int(rent_hour))
            total_price = price_per_hour * rent_hour
            rental_list = get_rentals()
            increment = len(rental_list)
            new_rental = [
                f"R{increment:03}",
                username,
                user_car,
                str(pickup_date),
                str(return_date),
                str(total_price),
                "Pending",
                "False",
                "False",
                "False",
            ]
            #Adding Booking
            with open("rental_list.txt", "a") as wf:
                wf.write(list_to_string(new_rental) + "\n")
                clear()
            headers = rental_list[0]
            print("=" * 210)
            print(display_list(headers[:-2], 20))
            print("-" * 168)
            print(display_list(new_rental[:-2], 20))
            print("You have booked successfully.")
            print("You will be redirect to user menu page....")
            return
        else:
            print("This car is not available for renting at this time range.Please try again.")


def booking_payment(username):
    #Initialization
    clear()
    booking_exist = False
    booking_list = get_rentals()
    #Menu Interface
    print("=" * 210)
    print("Booking List".center(210))
    print("=" * 210)
    print(display_list(booking_list[0], 19))
    print("-" * 200)
    #Displaying bookings
    is_displayed = False
    for records in booking_list:
        if records[1] == username and records[6] == "Pending" and records[7] == "False":
            is_displayed = True
            print(display_list(records, 19))
    if not is_displayed:
        print("(No booking found.)")
    print("(Note: Enter 'exit' to quit to menu.)")
    #Selecting Booking
    while booking_exist == False:
        print("=" * 210)
        user_rental_id = input("Please enter the RentalID of the car you would like to pay for: ").capitalize()
        if user_rental_id.lower() == "exit":
            clear()
            return
        else:
            for record in booking_list:
                if (record[0] == user_rental_id
                    and record[1] == username
                    and record[6] == "Pending"
                    and record[7] == "False"
                ):
                    booking_exist = True
        if booking_exist == False:
            print("Booking does not exist.")
    #Validating payment method for payment
    payment_method = validating_payment_method()
    payment_date = datetime.datetime.now().replace(microsecond=0)
    clear()
    print("=" * 210)
    print("Payment Successful. Your Rental Detail:")
    #Generating Payment
    for record in booking_list:
        if record[0] == user_rental_id:
            record[7] = "Paid"
            record[8] = payment_method.title()
            record[9] = str(payment_date)
            print(display_list(booking_list[0], 19))
            print("-" * 200)
            print(display_list(record, 19))
    #Updating Payment
    with open("rental_list.txt", "w") as wf:
        for i in range(len(booking_list)):
            wf.write(list_to_string(booking_list[i]) + "\n")
    print("You will be directed back to the menu...")
    return


def booking_cancellation(username):
    #Initialization
    got_record = False
    booking_exist = False
    booking_list = get_rentals()
    headers = booking_list[0]
    #Menu Interface
    print("=" * 210)
    print("Booking List".center(210))
    print("=" * 210)
    print(display_list(booking_list[0], 19))
    print("-" * 200)
    #Display Bookings
    for records in booking_list:
        if (
            records[1] == username
            and records[6] == "Pending"
            and records[7] == "False"
        ):
            print(display_list(records, 19))
            got_record = True
    if got_record == False:
        print("(Record not found.)")
        confirmation = ""
        while not confirmation == "y":
            print("=" * 210)
            confirmation = input("Enter y to exit to menu: ").lower()
            if confirmation == "y":
                clear()
                return
            else:
                print("Please Enter y only.")
    print("(Note: Enter 'exit' to quit to menu.)")
    #Selecting Booking
    while booking_exist == False:
        print("=" * 210)
        user_rental_id = input(
            "Please enter the RentalID of the car you would like to cancel: "
        ).capitalize()
        if user_rental_id.lower() == "exit":
            clear()
            return
        else:
            for record in booking_list:
                if (
                    record[0] == user_rental_id
                    and record[1] == username
                    and record[7] == "False"
                ):
                    booking_exist = True
        if booking_exist == False:
            print("Booking does not exist.")
    clear()
    print("=" * 210)
    #Cancelling selected booking
    for record in booking_list:
        if record[0] == user_rental_id:
            record[6] = "Cancelled"
            print(display_list(headers[:-3], 19))
            print("-" * 140)
            print(display_list(record[:-3], 19))
    #Updating booking status
    with open("rental_list.txt", "w") as wf:
        for i in range(len(booking_list)):
            wf.write(list_to_string(booking_list[i]) + "\n")
    print(f"Booking({user_rental_id}) is cancelled successfully.")
    print("You will be directed back to the menu...")
    return


# Menu for Admin
def admin_menu():
    while True:
        # Menu Interface for Admin
        print("=" * 210)
        print("ADMIN MENU".center(210))
        print("=" * 210)
        print("Option 1 : View Users")
        print("Option 2 : View Rented Cars")
        print("Option 3 : View Available Cars")
        print("Option 4 : View Customer Bookings")
        print("Option 5 : View Customer Payment")
        print("Option 6 : Add Cars")
        print("Option 7 : Cancel Outdated Bookings")
        print("Option 8 : Update Rental Status")
        print("Option 9 : Modify Car Details")
        print("Option 10: Exit to Home Page")
        print("=" * 210)
        is_valid = False
        while not is_valid:
            # Actions
            option = get_int("Enter your option: Option ")
            if option == 1:
                is_valid = True
                clear()
                view_users()
            elif option == 2:
                is_valid = True
                clear()
                view_rented_cars()
            elif option == 3:
                is_valid = True
                clear()
                view_available_cars_for_admin()
            elif option == 4:
                is_valid = True
                clear()
                view_customer_bookings()
            elif option == 5:
                is_valid = True
                clear()
                view_customer_payments()
            elif option == 6:
                is_valid = True
                clear()
                add_car()
            elif option == 7:
                is_valid = True
                clear()
                outdated_booking_cancellation()
            elif option == 8:
                is_valid = True
                clear()
                update_rental_status()
            elif option == 9:
                is_valid = True
                clear()
                modify_car_detail()
            elif option == 10:
                is_valid = True
                clear()
                return
            # Invalid Input
            else:
                print("Please enter a number within the given options.")
                print("=" * 210)


# Menu for Registered customer
def registered_user_menu(username):
    while True:
        # Menu interface
        print("=" * 210)
        print("USER MENU".center(210))
        print("=" * 210)
        print("Option 1: Modify Personal Details")
        print("Option 2: View Rental History")
        print("Option 3: View Available Cars")
        print("Option 4: Booking a car")
        print("Option 5: Booking Payment")
        print("Option 6: Booking Cancellation")
        print("Option 7: Exit to Home Page")
        print("=" * 210)
        is_valid = False
        while not is_valid:
            # Actions
            option = get_int("Enter your option: Option ")
            if option == 1:
                is_valid = True
                clear()
                modify_detail(username)
            elif option == 2:
                is_valid = True
                clear()
                rental_history(username)
            elif option == 3:
                is_valid = True
                clear()
                view_available_cars()
            elif option == 4:
                is_valid = True
                clear()
                booking(username)
            elif option == 5:
                is_valid = True
                clear()
                booking_payment(username)
            elif option == 6:
                is_valid = True
                clear()
                booking_cancellation(username)
            elif option == 7:
                is_valid = True
                clear()
                return
            # Invalid Input
            else:
                print("Please enter a number within the given options.")
                print("=" * 210)


# Menu for Guest
def guest_menu():
    while True:
        # Menu interface for guest
        print("=" * 210)
        print("GUEST MENU".center(210))
        print("=" * 210)
        print("Option 1: View Available Cars")
        print("Option 2: Register as User")
        print("Option 3: Exit to Home Page")
        print("=" * 210)
        is_valid = False
        while not is_valid:
            # Actions
            option = get_int("Enter your Option   : Option ")
            if option == 1:
                is_valid = True
                clear()
                view_available_cars()
            elif option == 2:
                is_valid = True
                clear()
                registration()
            elif option == 3:
                is_valid = True
                clear()
                return
            # Invalid Input
            else:
                print("Please enter a number within the given options.")
                print("=" * 210)


# home page of SCRS
def home_page():
    while True:
        # Menu Interface for Home Page
        print("=" * 210)
        print("Welcome to SUPER CAR RENTAL SERVICES!".center(210))
        print("=" * 210)
        print(
            "(Note: You are advised to open this program in full screen-mode to have better user experience.)"
        )
        print("Hi user, please choose either one of the following options.")
        print("Option 1: Login")
        print("Option 2: Visit as guest")
        print("Option 3: Exit")
        print("=" * 210)
        is_valid = False
        while not is_valid:
            # Action
            option = get_int("Enter your option : Option ")
            if option == 1:
                is_valid = True
                clear()
                login()
            elif option == 2:
                is_valid = True
                clear()
                guest_menu()
            elif option == 3:
                exit()
            # invalid input
            else:
                print("Please enter a number within the given options.")
                print("=" * 210)


# main program
home_page()