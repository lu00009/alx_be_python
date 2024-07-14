def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice.isdigit() and int(choice) in range(1, 5):
            choice = int(choice)
            if choice == '1':
                item = input("Enter the item name: ")
                shopping_list.append(item)
                print(f"'{item}' has been added to the list.")
                pass
            elif choice == '2':
                item = input("Enter an item you want to remove: ")
                if item in shopping_list:
                    shopping_list.remove(item)
                    print(f"'{item}' has been removed from the list.")
                else:
                    print(f"'{item}' not found in the list.")
                pass
            elif choice == '3':
                if shopping_list:
                    print("\nCurrent shopping list:")
                    for index, item in enumerate(shopping_list, start=1):
                        print(f"{index}. {item}")
                else:
                    print("The shopping list is empty.")
                pass
            elif choice == '4':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        else:  
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
