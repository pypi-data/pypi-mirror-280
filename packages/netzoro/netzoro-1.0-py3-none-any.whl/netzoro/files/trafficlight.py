from abc import ABC, abstractmethod

class Traffic_light:
    state = None
    def __init__(self, state):
        self.setTrffic_light(state)
    def setTrffic_light(self, state):
        self.state = state
        self.state.Traffic_light = self
    def presentState(self):
        print(f"Traffic_light is in {type(self.state).__name__}")
    def Color_state(self):
        self.state.Color_state()
    def function_state(self):
        self.state.function_state()


class Traffic_light_state(ABC):

    @property
    def Traffic_light(self):
        return self._Trffic_light

    @Traffic_light.setter
    def Traffic_light(self, Traffic_light):
        self._Trffic_light = Traffic_light

    @abstractmethod
    def Color_state(self):
        pass

    @abstractmethod
    def function_state(self):
        pass


class Red(Traffic_light_state): # Stops the vehicle

    def Color_state(self):
        print("Traffic light is already in 'red'")

    def function_state(self):
        print("You need to stop")
        self.Traffic_light.setTrffic_light(Yellow())
    

class Yellow(Traffic_light_state): # Alerts the vehicle

    def Color_state(self):
        print("Traffic light is already in 'yellow'")
        self.Traffic_light.setTrffic_light(Red())

    def function_state(self):
        print("Get ready to go")
    
class Green(Traffic_light_state): # Allows the vehicle to move

    def Color_state(self):
        print("Traffic light is already in 'green'")
    
    def function_state(self):
        print("You can go now")

if __name__ == "__main__":
    
    myTraffic_light = Traffic_light(Red())
    myTraffic_light.presentState()
    myTraffic_light.Color_state()
    myTraffic_light.function_state()

    myTraffic_light = Traffic_light(Yellow())
    myTraffic_light.presentState()
    myTraffic_light.Color_state()
    myTraffic_light.function_state()

    myTraffic_light = Traffic_light(Green())
    myTraffic_light.presentState()
    myTraffic_light.Color_state()
    myTraffic_light.function_state()