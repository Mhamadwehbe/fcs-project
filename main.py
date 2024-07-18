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


def cities_menu():