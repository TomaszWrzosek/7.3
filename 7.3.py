class Car:
    def __init__(self, make, model_name, top_speed, color):
       self.make = make
       self.model_name = model_name
       self.top_speed = top_speed
       self.color = color
        # Variables
       self.current_speed = 0
    def __str__(self):
        return f'{self.color} {self.make} {self.model_name}'
    def __repr__(self):
        return f"Car(make={self.make} model={self.model_name}, top_speed={self.top_speed}, color={self.color})"

    def __eq__(self, other):
        return all(
            (
            self.make == other.make,
            self.model_name == other.model_name,
            self.top_speed == other.top_speed,
            self.color == other.color
            )
        )
    def __gt__(self, other):
        return self.top_speed > other.top_speed

    def accelerate(self, step=10):
        self.current_speed += step

    def decelerate(self, step=10):
        self.current_speed -= step
    @property
    def current_speed(self):
        return self._current_speed

    @current_speed.setter
    def current_speed(self, value):
        if value <= self.top_speed:
            self._current_speed = value
        else:
            raise ValueError(f"Value {value} exceeds top speed of {self.top_speed}")

class Truck(Car):
   def __init__(self, max_load, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.max_load = max_load

truck = Truck(make="Mercedes", model_name="Actros", color="Black", top_speed=90, max_load=1200)
print(truck)
truck.accelerate(10)
print(truck.current_speed)

truck = Truck(make="Mercedes", model_name="Sprinter", color="Black", top_speed=90, max_load=1200)
car = Car(make="Ford", model_name="Mustang", top_speed=250, color="red")
print(isinstance(Truck, Car))

car_one = Car(make = "Ford", model_name="Mustang", top_speed=250, color="Red")
car_two = Car(make ="Ford", model_name="Fiesta", top_speed=200, color="Blue")
car_three = Car(make ="Porsche", model_name="911", top_speed=320, color="Black")
cars = [car_one, car_two, car_three]
by_speed = sorted(cars, key=lambda car: car.top_speed)
by_make = sorted(cars, key=lambda car: car.make)
