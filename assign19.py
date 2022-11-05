income=int(input("Enter the annual income"))

if income<=250000:
    print("You have to pay no tax")
elif 250000<income<=500000:
    tax=income*0.05
    print(f"Income tax amount = {tax}")
elif 500000<income<=1000000:
    tax=income*0.2
    print(f"Income tax amount = {tax}")
elif 1000000<income<=5000000:
    tax=income*0.3
    print(f"Income tax amount = {tax}")
else:
    print("Contact Income tax")