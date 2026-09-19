print("Calculate fuel consumtion.")
Feed = input("Enter the distance in kilometers:")
Distance = int(Feed)
Feed = input("Enter fuel usage(liters): ")
FuelUsage = int(Feed)
consumption = (FuelUsage / Distance) * 100
consumption = int(consumption)
print(f"Fuel consumption is {consumption} liters per 100 km.")


