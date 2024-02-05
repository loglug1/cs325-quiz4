class WeatherWidget():
    def __init__(self, cond: str, temp: int):
        self.temperature = temp
        self.condition = cond
    
    @property
    def temperature(self):
        return self._temperature
    
    @temperature.setter
    def temperature(self, temp):
        self._temperature = temp

    @property
    def condition(self):
        return self._condition
    
    @condition.setter
    def condition(self, cond):
        self._condition = cond

    def print(self):
        print(f"""
              =========================
              {self.temperature} degrees
              and {self.condition}
              =========================
              """)
        


def main():
    widget = WeatherWidget('Sunny', 65)
    widget.print()

    widget.condition = 'Windy'
    widget.print()

    widget.temperature = 50
    widget.print()

if __name__=='__main__':
    main()