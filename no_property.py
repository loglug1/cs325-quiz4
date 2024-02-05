class WeatherWidget():
    def __init__(self, cond: str, temp: int):
        self.set_temperature(temp)
        self.set_condition(cond)
    
    def get_temperature(self):
        return self._temperature
    
    def set_temperature(self, temp):
        self._temperature = temp

    def get_condition(self):
        return self._condition
    
    def set_condition(self, cond):
        self._condition = cond

    def print(self):
        print(f"""
              =========================
              {self.get_temperature()} degrees
              and {self.get_condition()}
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