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

        if choice == '1':
            show_cities()
        elif choice == '2':
            print_neighboring_cities()
        elif choice == '3':
            print_drivers_delivering_to_city
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")


    
def view_all_drivers():
    if not drivers:
        print("No drivers found.")
    else:
        for driver in drivers:
            print(f"{driver['id']}, {driver['name']}, {driver['start_city']}")

def add_driver():
    name = input("Enter the driver's name: ")
    start_city = input("Enter the driver's start city: ")

    if start_city not in cities:
        add_city = input(f"City {start_city} not found. Would you like to add it? (yes/no): ").strip().lower()
        if add_city == 'yes':
            cities[start_city] = []
            print(f"City {start_city} added.")
        else:
            print("Driver not added. Start city must be in the database.")
            return

    new_id = f"ID{len(drivers) + 1:03}"
    drivers.append({'id': new_id, 'name': name, 'start_city': start_city})
    print(f"Driver {name} added with ID {new_id}.")


def show_cities():
    if not cities:
        print("No cities found.")
    else:
        for city in cities:
            print(city)

def print_neighboring_cities():
    city = input("Enter the city name: ")
    if city in cities:
        print(f"Neighboring cities for {city}: {', '.join(cities[city])}")
    else:
        print(f"City {city} not found in the database.")

def print_drivers_delivering_to_city():
    target_city = input("Enter the city name: ")

    def bfs(city):
        visited = set()
        queue = [city]

        while queue:
            current_city = queue.pop(0)
            if current_city not in visited:
                visited.add(current_city)
                queue.extend(cities.get(current_city, []))

        return visited

    reachable_cities = bfs(target_city)

    delivering_drivers = [driver for driver in drivers if driver['start_city'] in reachable_cities]

    if delivering_drivers:
        for driver in delivering_drivers:
            print(f"{driver['id']}, {driver['name']}, {driver['start_city']}")
    else:
        print(f"No drivers delivering to {target_city}.")

if __name__ == "__main__":
    main_menu()