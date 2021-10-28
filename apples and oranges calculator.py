print("The apple = 20 pesos orange = 25 pesos")
apple = 20
orange = 25
apples_ordered = int(input("How many apples do you want to buy?: "))
oranges_ordered = int(input("How many oranges do you want to buy?: "))
ApplePrice = apple * apples_ordered
OrangePrice = orange * oranges_ordered
total_amount = ApplePrice + OrangePrice
print(f"The total amount is {total_amount}.")