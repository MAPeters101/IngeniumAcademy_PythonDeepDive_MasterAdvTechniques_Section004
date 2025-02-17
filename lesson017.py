

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

