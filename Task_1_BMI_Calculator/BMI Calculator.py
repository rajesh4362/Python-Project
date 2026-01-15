
def welcome_message():
    print("============================================")
    print("          WELCOME TO BMI CALCULATOR          ")
    print("============================================")
    print("BMI is calculated using the formula:")
    print("BMI = Weight (kg) / Height (m)²")
    print("--------------------------------------------\n")


def get_valid_input(message):
    while True:
        try:
            value = float(input(message))
            if value <= 0:
                print(" Please enter a value greater than zero.\n")
            else:
                return value
        except ValueError:
            print(" Invalid input! Please enter numbers only.\n")


def calculate_bmi(weight, height):
    bmi = weight / (height * height)
    return bmi


def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi >= 18.5 and bmi < 25:
        return "Normal Weight"
    elif bmi >= 25 and bmi < 30:
        return "Overweight"
    else:
        return "Obesity"


def display_output(bmi, category):
    print("\n================ BMI RESULT ================")
    print(f"Your BMI Value  : {bmi:.2f}")
    print(f"BMI Category   : {category}")
    print("============================================\n")


def main():

    while True:
        weight = get_valid_input("Enter your weight in kilograms (kg): ")
        height = get_valid_input("Enter your height in meters (m): ")

        bmi = calculate_bmi(weight, height)
        category = bmi_category(bmi)

        display_output(bmi, category)

        again = input("Do you want to calculate BMI again? (yes/no): ").lower()
        if again != "yes":
            print("\nThank you for using the BMI Calculator ")
            print("Have a healthy day!")
            break
main()
