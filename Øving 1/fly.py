from math import *

def hotel_cost(nights):
    return nights * 140

print (hotel_cost(10))

def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475

print (plane_ride_cost("Tampa"))

def rental_car_cost(days):
    carcost = 40 * days
    if days >= 7:
        carcost -= 50
    elif 3<=days<7:
        carcost -= 20
    return carcost

print (rental_car_cost(3))

def trip_cost(city, days):
    return (sum(rental_car_cost(days), hotel_cost(days), plane_ride_cost(city)))

print (trip_cost(ctiy, days))
