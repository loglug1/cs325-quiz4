from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    @abstractmethod
    def turn_off(self):
        pass

class Desktop(Computer):
    def turn_on(self):
        print('Starting fans')
        print('Outputing to VGA')
    
    def turn_off(self):
        print('Video output ended')
        print('Shutting off fans')

class Laptop(Computer):
    def __init__(self,charged: bool):
        self.charged = charged

    def turn_on(self):
        if self.charged:
            print('Starting fans')
            print('Power on screen')
            self.charged == False
        else:
            print('Insufficient Battery, Please Plug in')
    
    def turn_off(self):
        print('Video output ended')


def main():
    pc = Desktop()
    pc.turn_on()
    pc.turn_off()

    notebook = Laptop(True)
    notebook.turn_on()
    notebook.turn_off()

if __name__=="__main__":
    main()