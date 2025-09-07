# expense_splitter.py

# Inputs (integers or floats allowed)
rent = float(input("Enter Your Rent: "))
food = float(input("Enter the Amount of food ordered: "))
electricity_spend = float(input("Enter the Electricity bill units spent: "))
charge_per_unit = float(input("Enter the Charge per unit: "))
persons = int(input("Enter the Total Persons Living in the Room: "))

# Validation
if persons <= 0:
    print("Error: Number of persons must be at least 1.")
else:
    total_electricity_cost = electricity_spend * charge_per_unit
    total_amount = rent + food + total_electricity_cost
    total_amount_per_person = total_amount / persons

    # Output with 2 decimal places
    print(f"\nTotal rent: {rent:.2f}")
    print(f"Total food: {food:.2f}")
    print(f"Electricity units: {electricity_spend:.2f} at {charge_per_unit:.2f} per unit")
    print(f"Total electricity cost: {total_electricity_cost:.2f}")
    print(f"Total amount (rent + food + electricity): {total_amount:.2f}")
    print(f"\nTotal amount each person should pay: {total_amount_per_person:.2f}")
