from abc import ABC, abstractmethod   # using abstraction to manage ride sharing operations


class Driver:                    
    def __init__(self,name):
        self.name = name
        self.available = True   # I use self.available to determine whether the driver is available for
                                # their customers. The Driver state is managed using Encapsulation and SRP.

    def occupied(self):
        self.available = False

class Customer:
    def __init__(self,name):     # I use this to represent a customer who books a ride. Once again 
        self.name = name         # using SRP.

class Ride(ABC):
    def __init__(self,distance):
        self.distance = distance

    @abstractmethod
    def calculate_ridefare(self):
        pass

class Economy_Ride(Ride):
    def calculate_ridefare(self):  # Inheritance is at play here as the code inherits from ride
        return self.distance * 5   # Each ride has its own implementation of calculate_ridefare()

class Luxury_Ride(Ride):
    def calculate_ridefare(self):
        return self.distance * 10

class Pool_Ride(Ride):
    def calculate_ridefare(self):
        return self.distance * 3    
    
class RideDrivingService:
    def __init__(self, drivers):
        self.drivers = drivers

    def get_driver(self):
        for driver in self.drivers:
            if driver.available:
                return driver
        return None
    
    def bookride(self, customer, pickup, dropoff, ride): # I used polymorphism particularly for ride
        driver = self.get_driver()                       # in this situation

        if driver is None:
            print("No drivers available")
            return
                                                      #ride can be either Economy_Ride,Luxury_Ride or Pool_Ride
        fare = ride.calculate_ridefare()
        driver.occupied()

        print(f"Ride Fare: ${fare}, Driver: {driver.name}")
    

    #Testing this code to hopefully to gain results as seen in Canvas
driver1 = Driver("Alice")
driver2 = Driver("Bob")

John = Customer("John")
Rebecca = Customer("Rebecca")
Mike = Customer("Mike")

service = RideDrivingService([driver1, driver2])
service.bookride(John, "Airport", "Downtown", Economy_Ride(15))
service.bookride(Rebecca, "College", "Downtown", Luxury_Ride(10))
service.bookride(Mike, "Downtown", "Shopping Mall", Pool_Ride(5))
    
