principal_amount=int(input("Enter principal amount :"))
interest_rate=float(input("Enter interest rate : "))
number_of_years=float(input("Enter number of years : "))
simple_interest=(principal_amount*interest_rate*number_of_years)/100
print(f"The calculated simple interest is {simple_interest}")
