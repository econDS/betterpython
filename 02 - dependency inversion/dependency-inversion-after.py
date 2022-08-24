from abc import ABC, abstractmethod


class Switchable(ABC):
    @abstractmethod
    def turn_on(self) -> None:
        pass

    @abstractmethod
    def turn_off(self) -> None:
        pass


class LightBulb(Switchable):
    def turn_on(self) -> None:
        print("LightBulb: turned on...")

    def turn_off(self) -> None:
        print("LightBulb: turned off...")


class Fan(Switchable):
    def turn_on(self):
        print("Fan: turned on...")

    def turn_off(self):
        print("Fan: turned off...")


class ElectricPowerSwitch:
    def __init__(self, client: Switchable):
        self.client: Switchable = client
        self.on: bool = False

    def press(self):
        if self.on:
            self.client.turn_off()
            self.on = False
        else:
            self.client.turn_on()
            self.on = True


lightBulb = LightBulb()
fan = Fan()
switch = ElectricPowerSwitch(fan)
switch.press()
switch.press()
