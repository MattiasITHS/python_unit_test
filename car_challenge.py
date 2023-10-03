class Car:
    def __init__(self):
        self.speed = 0
        self._start_car = False

    def start_car(self):
        if self._start_car:
            raise Exception("Car is already on")
        self._start_car = True

    def turn_off_car(self):
        self._start_car = False

    def add_speed(self):
        self.speed += 5

    def current_speed(self):
        return self.speed

    def stop(self):
        self.speed = 0

    def car_status(self):
        return self._start_car

    def remove_speed(self):
        if self.speed <= 0:
            self.speed = 0
        else:
            self.speed -= 5
