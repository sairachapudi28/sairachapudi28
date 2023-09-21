import datetime

def get_current_year():
    # Get the current year
    current_date = datetime.datetime.now()
    return current_date.year

def calculate_age(birth_year):
    # Calculate the user's age based on their birth year
    current_year = get_current_year()
    age = current_year - birth_year
    return age

def main():
    print("Welcome to the Age Calculator App!")
    
    # Get the user's name
    name = input("Please enter your name: ")
    
    # Get the user's birth year
    try:
        birth_year = int(input("Please enter your birth year: "))
    except ValueError:
        print("Invalid input. Please enter a valid year.")
        return

    age = calculate_age(birth_year)
    
    # Greet the user and display their age
    print(f"Hello, {name}!")
    print(f"You are {age} years old.")

if __name__ == "__main__":
    main()
