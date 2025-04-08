class Aircrafts:
    def __init__(self, thrust, lift, max_speed):
        self.thrust = thrust
        self.lift = lift
        self.max_speed = max_speed

    def show_technical_specs(self):
        print(f"Thrust: {self.thrust}")
        print(f"Lift: {self.lift}")
        print(f"Maximum speed: {self.max_speed}")


class Helicopter(Aircrafts):
    def __init__(self, thrust, lift, max_speed, no_of_rotors):
        super().__init__(thrust, lift, max_speed)
        self.no_of_rotors = no_of_rotors

    def show_technical_specs(self):
        super().show_technical_specs()
        print(f"Number of rotors: {self.no_of_rotors}")