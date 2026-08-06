from colorama import init
init(autoreset=True)

import expenses
import weather
import todo
import country_info

while True:
    print("\n=== Personal Dashboard ===")
    print("1. Expenses")
    print("2. Weather")
    print("3. To-Do List")
    print("4. Country Information")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        expenses.run_menu()
    elif choice == "2":
        weather.check_weather()
    elif choice == "3":
        todo.run_menu()
    elif choice == "4":
        country = input("Enter country name: ")
        country_info.get_country_info(country)  
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option, try again.")
