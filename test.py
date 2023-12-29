def fruit_parts():
    fruits = {
        'apple': ["seed"],
        'orange': ["feed"],
        'banana': ["keep"]
    }

    choice = choose_fruit()  # Call the choose_fruit function to get the choice
    if choice == 1:
        selected_fruit = 'apple'
    elif choice == 2:
        selected_fruit = 'orange'
    elif choice == 3:
        selected_fruit = 'banana'
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
        return

    # Access the selected fruit's array from the fruits dictionary
    selected_array = fruits[selected_fruit]

    # Print the result or perform further actions with the selected array
    print(f"The selected fruit is: {selected_fruit}")
    print(f"The corresponding array is: {selected_array}")

def choose_fruit():
    choice = input("Enter your choice (1 for apple, 2 for orange, or 3 for banana): ")
    try:
        choice = int(choice)
        if choice not in [1, 2, 3]:
            raise ValueError("Invalid choice. Please enter 1, 2, or 3.")
    except ValueError as e:
        print(e)
        return choose_fruit()  # Recursively call choose_fruit until a valid choice is made

    return choice

# Call the fruit_parts function to run the program
fruit_parts()
