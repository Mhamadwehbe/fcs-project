drivers = []
cities = {}


def main_menu():
    while True:
        print("Hello! Please enter:")
        print("1. To go to the drivers' menu")
        print("2. To go to the cities' menu")
        print("3. To exit the system")

        choice = input("Your choice: ")

        if choice == '1':
            drivers_menu()
        elif choice == '2':
            cities_menu()
        elif choice == '3':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

def drivers_menu():
    while True:
        print("Enter:")
        print("1. To view all drivers")
        print("2. To add a driver")
        print("3. To go back to main menu")

        choice = input("Your choice: ")

        if choice == '1':
            view_all_drivers()
        elif choice == '2':
            add_driver()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def cities_menu():
    while True:
        print("Enter:")
        print("1. Show cities")
        print("2. Print neighboring cities")
        print("3. Print drivers delivering to city")
        print("4. To go back to main menu")

        choice = input("Your choice: ")
