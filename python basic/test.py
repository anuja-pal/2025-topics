from circle import Circle

c1 = Circle(5)
c2 = Circle(4)

vars(c1)
vars(Circle)
# print("The area of the first circle is: ",c1.__area())
# print("The area of the second circle is: ",c2.__area())

from sample_class import SampleClass
sample_instance = SampleClass("Hello!")
vars(sample_instance)
vars(SampleClass)


from square import Square
s = Square(5)
vars(s)
vars(Square)

s._Square__area()


from obj_count import ObjectCounter
o1 = ObjectCounter()
o2 = ObjectCounter()

ObjectCounter.no_of_objects

o3 = ObjectCounter()

ObjectCounter.no_of_objects
o3.no_of_objects


from vehicles import Car, Bike
my_car = Car(make="Honda",model="City",year="2020",no_of_wheels=4)
my_bike = Bike(make="Ducati",model="Ascension",year="2023",colour="red")


print(my_car)
print(my_bike)

my_car.start()
my_car.stop()
my_car.drive()
my_bike.ride()

vars(my_bike)
vars(Bike)

vars(my_car)
vars(Car)

from aircrafts import Helicopter
my_copter = Helicopter(thrust = 90, lift = 40, max_speed = 100, no_of_rotors = 9)
my_copter.show_technical_specs()

from workers import Manager
my_first_reportee = Manager(name="AP",id="1041234",department="Data Science",hourly_salary=40,hourly_bonus=5)
my_first_reportee.display_profile()
my_first_reportee.calculate_salary(hours_worked=10)