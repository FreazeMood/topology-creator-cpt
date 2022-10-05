import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from interface import Interface
from ratios import ROUTER_X_RATIO, ROUTER_Y_RATIO
import pyautogui as pya


class Router(Interface):

    def __init__(self, directory) -> None:
        super().__init__(directory)
        self.router_location = self.find_icon_location(ROUTER_X_RATIO, ROUTER_Y_RATIO)
        
    def take_and_put(self, qty: int) -> None:
        super().take_and_put()
        router_counter = 0
        initial_qty = qty

        while initial_qty > 0:
            router_counter += 1
            pya.moveTo(x=self.router_location['x'], y=self.router_location['y'])
            x_target, y_target = (self.resolution['x'] // (qty * 1.35)) * router_counter, (self.resolution['y'] // 4)
            pya.dragTo(x=x_target, y=y_target, button='left')
            initial_qty -= 1 


if __name__ == '__main__':
    router = Router('D:\\pc shit\\Cisco Packet Tracer 8.0\\bin\\PacketTracer.exe')
    router.take_and_put(7)
