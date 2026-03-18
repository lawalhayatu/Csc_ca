from abc import ABC, abstractmethod

# 1. Abstract Base Class
class StationAsset(ABC):
    def __init__(self, name):
        self.name = name

    # 3. Abstraction: force subclasses to implement this
    @abstractmethod
    def calculate_revenue(self):
        pass


# 2. FuelDispenser class
class FuelDispenser(StationAsset):
    def __init__(self, name, price_per_liter, liters_sold):
        super().__init__(name)
        self.price_per_liter = price_per_liter
        self.liters_sold = liters_sold

    # 3. Polymorphism: different logic
    def calculate_revenue(self):
        return self.price_per_liter * self.liters_sold


# 2. CarWash class
class CarWash(StationAsset):
    def __init__(self, name, cars_washed, price_per_car):
        super().__init__(name)
        self.cars_washed = cars_washed
        self.price_per_car = price_per_car

    # 3. Polymorphism: different logic
    def calculate_revenue(self):
        return self.cars_washed * self.price_per_car