def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price
    

#prompting the user

price = float(input("Enter the Price: "))
discount_percent = float(input("Enter the Discount allowed: "))

final_price = calculate_discount(price,discount_percent)

#Displaying the output

if final_price == price:
    print(f"No Discount Applied, The Total Amount is {price}")

else:
    print(f"After a {discount_percent} % discount, The Total amount is {final_price}")

