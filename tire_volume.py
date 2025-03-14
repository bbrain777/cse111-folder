import math
from datetime import datetime

# Tire price lookup table 
TIRE_PRICES = {
    (185, 50, 14): 75.99,
    (205, 60, 15): 89.99,
    (225, 65, 16): 105.50,
    (255, 55, 17): 129.99,
}

# Function to calculate tire volume
def calculate_tire_volume(width, aspect_ratio, diameter):
    volume = (math.pi * (width ** 2) * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000
    return volume

# Main function
def main():
    # Get user inputs
    width = int(input("Enter the width of the tire in mm (ex 205): "))
    aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
    diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

    # Calculate the volume
    volume = calculate_tire_volume(width, aspect_ratio, diameter)
    print(f"The approximate volume is {volume:.2f} liters")

    # Get current date
    current_date = datetime.now().strftime("%Y-%m-%d")

    # Check for tire price
    tire_key = (width, aspect_ratio, diameter)
    price = TIRE_PRICES.get(tire_key, "Not available")

    if price != "Not available":
        print(f"The price for this tire size is ${price:.2f}")
    else:
        print("Sorry, we do not have pricing for this size.")

    # Ask if the user wants to buy the tire
    buy_tire = input("Would you like to buy this tire? (yes/no): ").strip().lower()

    # Append results to volumes.txt
    with open("volumes.txt", "a") as file:
        if buy_tire == "yes":
            phone_number = input("Please enter your phone number: ")
            file.write(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}, ${price}, {phone_number}\n")
        else:
            file.write(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}, ${price}\n")

    print("Thank you! Your data has been recorded.")

# Run the program
if __name__ == "__main__":
    main()
