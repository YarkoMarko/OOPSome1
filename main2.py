class TemperatureSensor:
    def __init__(self, temperature):
        self.__temperature = temperature

    @property
    def temp(self):
        return self.__temperature

    @temp.setter
    def temp(self, temperature):
        if -10 < temperature < 90:
            self.__temperature = temperature

        else:
            raise ValueError("Wrong value of temperature")


t = TemperatureSensor(20)

print(t.temp)

t.temp = 0

print(t.temp)
