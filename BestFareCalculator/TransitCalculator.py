import math


# initiating class
class TransitCalculator:
    fare_options = ["Pay-per-ride", "7-day Unlimited", "30-day Unlimited"]
    fares = [2.75, 33.0, 127.0]
    fares_reduced = [1.35, 16.50, 63.50]

    # initiating a constructor
    def __init__(self, days, rides, age):
        self.days = days
        self.rides = rides
        self.age = age

    # checking reduced price options
    def is_eligible(self):
        if self.age > 65:
            return True

    # Method calculates overall cost of travel using 7 days Option
    def unlimited_7_price(self):
        seven_days_purchaces = math.ceil(self.days / 7)
        total_7_day_cost = seven_days_purchaces * TransitCalculator.fares[1]
        return total_7_day_cost / self.rides

    # Method calculates total cost of the rides
    def get_ride_prices(self):
        if self.is_eligible:
            ppr_price = TransitCalculator.fares_reduced[0]
            unlimited_7_price = self.unlimited_7_price()
            unlimited_30_price = TransitCalculator.fares_reduced[2] / self.rides
            prices65 = [ppr_price, unlimited_7_price, unlimited_30_price]
            return prices65
        else:
            ppr_price = TransitCalculator.fares[0]
            unlimited_7_price = self.unlimited_7_price()
            unlimited_30_price = TransitCalculator.fares[2] / self.rides
            prices65 = [ppr_price, unlimited_7_price, unlimited_30_price]
            return prices65

    # Methods finds the best fare
    def get_best_fare(self):
        ride_prices = self.get_ride_prices()
        winning_index = 0
        for i in range(len(ride_prices)):
            if ride_prices[i] < ride_prices[winning_index]:
                winning_index = i
        return "You should get the " + TransitCalculator.fare_options[winning_index] + " option at $" + \
               str(ride_prices[winning_index]) + " per ride. "


my_rides = 150
my_days = 30
my_age = 63
trans_cal = TransitCalculator(my_rides, my_days, my_age)
print(trans_cal.get_best_fare())
