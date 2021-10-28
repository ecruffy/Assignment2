MoneyInWallet = int(input("How much money do you wish to spend?: "))
ApplePrice = int(input("How much does an apple cost?: "))
apples_you_can_buy = MoneyInWallet // ApplePrice
change = MoneyInWallet % ApplePrice
print(f"You can buy {apples_you_can_buy} apples and your change is {change} pesos")