from models import FuelDispenser, CarWash

def main():
    # 4. Create different assets
    assets = [
        FuelDispenser("Pump 1", price_per_liter=650, liters_sold=100),
        FuelDispenser("Pump 2", price_per_liter=650, liters_sold=150),
        CarWash("Wash Bay 1", cars_washed=20, price_per_car=2000),
        CarWash("Wash Bay 2", cars_washed=15, price_per_car=2000)
    ]

    total_revenue = 0

    # Loop through assets
    for asset in assets:
        revenue = asset.calculate_revenue()
        print(f"{asset.name} Revenue: ₦{revenue}")
        total_revenue += revenue

    print("\n--- Total Station Revenue ---")
    print(f"Total Revenue: ₦{total_revenue}")


if __name__ == "__main__":
    main()