# ------------------------------
# Assignment 1: Design Your Own Class
# ------------------------------

# Base class
class Device:
    def _init_(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        return f"{self.brand} {self.model}"


# Derived class (inheritance)
class Smartphone(Device):
    def _init_(self, brand, model, os, storage):
        super()._init_(brand, model)  # calling parent constructor
        self.os = os
        self.storage = storage

    def make_call(self, number):
        return f"📞 Calling {number} using {self.model}"

    def install_app(self, app_name):
        return f"⬇ Installing {app_name} on {self.model}"

    # Polymorphism: overriding parent method
    def info(self):
        return f"{self.brand} {self.model} ({self.os}, {self.storage}GB)"


# ------------------------------
# Assignment 2: Polymorphism Challenge
# ------------------------------

class Vehicle:
    def move(self):
        return "Vehicle is moving"

class Car(Vehicle):
    def move(self):
        return "🚗 Driving on the road"
class Plane(Vehicle):
    def move(self):
        return "✈ Flying in the sky"

class Boat(Vehicle):
    def move(self):
        return "🚤 Sailing on water"


# ------------------------------
# Main Program
# ------------------------------
if _name_ == "_main_":
    print("=== ASSIGNMENT 1: CUSTOM CLASS ===")
    phone1 = Smartphone("Samsung", "Galaxy S24", "Android", 256)
    phone2 = Smartphone("Apple", "iPhone 15", "iOS", 128)

    print(phone1.info())
    print(phone1.make_call("08012345678"))
    print(phone2.install_app("WhatsApp"))

    print("\n=== ASSIGNMENT 2: POLYMORPHISM CHALLENGE ===")
    vehicles = [Car(), Plane(), Boat()]
    for v in vehicles:
        print(v.move())
