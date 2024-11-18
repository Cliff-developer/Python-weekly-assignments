def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    If the discount is 20% or higher, apply the discount.
    Otherwise, return the original price.
    """
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    return price


try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(original_price, discount_percentage)
    if final_price < original_price:
        print(f"The final price after the discount is applied is : ksh{final_price:.2f}")
    else:
        print(f"No discount applied. The original price is: ksh{original_price:.2f}")
except ValueError:
    print("Invalid input! Please enter numeric values for the price and discount percentage.")
