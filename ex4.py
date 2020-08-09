cars = 100
space_in_car = 4.0
drivers = 30
passengers = 70
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = int(cars_driven * space_in_car)
average_passenger_per_car = int(passengers / cars_driven)

print("There are", cars,"cars available")
print("There are", drivers,"drivers available" )
print("There will be", cars_not_driven, "empty cars today")
print("we can transport", carpool_capacity, "people today")
print("we have", passengers, "passengers today")
print("we have to put", average_passenger_per_car,"passengers in each car")
