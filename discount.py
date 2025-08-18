# Function to calculate discount
def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    If discount is 20% or higher, apply it.
    Otherwise, return the original price.
    """
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        return price


# Prompt user for input
try:
    price = float(input("Enter the original price: "))
    discount_percent = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(price, discount_percent)

    if discount_percent >= 20:
        print(f"Discount applied! The final price is: {final_price:.2f}")
    else:
        print(f"No discount applied. The price remains: {final_price:.2f}")

except ValueError:
    print("Invalid input. Please enter numbers only.")
