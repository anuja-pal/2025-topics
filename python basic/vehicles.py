class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self._started = False

    def start(self):
        print("Starting Engine...")
        self._started = True

    def stop(self):
        print("Stopping engine...")
        self._started = False


class Car(Vehicle):
    def __init__(self, make, model, year, no_of_wheels):
        super().__init__(make, model, year)
        self.no_of_wheels = no_of_wheels

    def drive(self):
        print(f"Driving my {self.make} - {self.model}, bought in the year {self.year}.")
        print(f"It has {self.no_of_wheels} wheels.")

    def __str__(self):
        return f"My {self.model} car is very nice!"
    

class Bike(Vehicle):
    def __init__(self, make, model, year, colour):
        super().__init__(make, model, year)
        self.colour = colour

    def ride(self):
        print(f"Riding my lovely {self.make} - {self.model} bike.")

    def __str__(self):
        return f"It is a {self.colour}ed bike."
    
    
    
