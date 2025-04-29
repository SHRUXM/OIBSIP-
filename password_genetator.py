import random
import string

def generate_password(lenght, use_letters, use_numbers, use_symbols):

    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Error: At least one character type must be selected."
    
    password = ''.join(random. choice(characters)for i in range(lenght))
    return password 
def get_user_preferences():

    length_str= input("Enter the desired password lenght:")
    if not length_str.isdigit():
        print("Invalid input. Please enter a number for the password lenght.")
        return None, None, None, None
    lenght = int(length_str)

    use_letters = input("Include letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    return lenght, use_letters, use_numbers, use_symbols

def main():

    lenght, use_letters, use_numbers, use_symbols = get_user_preferences()

    if lenght is None:
        reurn # Exit if input is invalid

    password = generate_password(lenght, use_letters, use_numbers, use_symbols)
    print("Genetrated password:", password)

if __name__ == "__main__":
    main()
    
                       