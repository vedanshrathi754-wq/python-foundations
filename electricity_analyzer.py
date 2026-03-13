# Electricity Usage Analyzer
# Estimates electricity consumption and cost of household appliances

appliances = {}

while True:
    print("\nElectricity Usage Analyzer")
    print("1. Add appliance usage")
    print("2. Show electricity report")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter appliance name: ")
        power = float(input("Power rating (Watts): "))
        hours = float(input("Hours used per day: "))

        monthly_units = (power * hours * 30) / 1000

        appliances[name] = monthly_units

        print(f"{name} monthly consumption: {monthly_units:.2f} units")

    elif choice == "2":
        total_units = sum(appliances.values())
        cost_per_unit = 8   # Example electricity price
        bill = total_units * cost_per_unit

        print("\nElectricity Report")
        for appliance, units in appliances.items():
            print(f"{appliance}: {units:.2f} units")

        print(f"\nTotal Units: {total_units:.2f}")
        print(f"Estimated Bill: ₹{bill:.2f}")

    elif choice == "3":
        print("Exiting analyzer.")
        break

    else:
        print("Invalid choice")
