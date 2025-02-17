

class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    @property
    def temperature(self):
        print("Getting temperature")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        print("Setting temperature")
        self._temperature = value

class Sunrise:
    sunrise_hour = None

    def __init__(self, day="Sunday"):
        self.day = day

    @staticmethod
    def set_today(today): # Can't access class or instance attributes or methods
        # self.day = today # Will throw an error
        return today

    @classmethod
    def set_sunrise_class_method(cls, hour): # Can access class attributes & methods
        cls.sunrise_hour = hour

    def set_sunrise(self, hour):
        self.sunrise_hour = hour  # Will create instance attribute but will not change class attribute



if __name__ == '__main__':
    c = Celsius(25)
    c.temperature = 30
    print(c.temperature)
