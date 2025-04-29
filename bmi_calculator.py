def calculate_bmi(weight, height):
    return weight / (height **2)

def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <24.9:
        return "Normal weight"
    elif 18.5<= bmi < 29.9:
        return "Overweight"
    else:
        return"Obese"
    

def main():
    try:
        weight = float(input("Enter your weight in kilomagrams: "))
        height = float(input("Enter your height in meters: "))

        if weight <= 0 or height <= 0:
            print("Invalid input. Weight and height must be positive numbers.")
            return
        bmi = calculate_bmi(weight, height)
        category = categorize_bmi(bmi)

        print(f"Your BMI is: {bmi:.2f}")
        print(f"Category:v {category}")

    except ValueError:
        print("Invalid input. Please enter numeric values for weight and height.")

if __name__ == "__main__":
    main()