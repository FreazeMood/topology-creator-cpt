from interface import Interface
from constants import ROUTRER_X_RATIO, ROUTRER_Y_RATIO
import pyautogui as pya

class Router(Interface):

    def __init__(self, directory) -> None:
        super().__init__(directory)
        self.router_location = self.define_router_location()
        
    def take_and_put(self, qty):
        
        if self.check_if_window_on_screen():
            self.define_screen_size()
            self.find_mouse_pos()
            print(self.current_position)

        else:
            raise TypeError

        while qty > 0:
            pya.moveTo(x=self.router_location['x'], y=self.router_location['y'])
            pya.dragTo(x=1274, y=650, button='left')
            qty -= 1 
    
    def define_router_location(self):

        width = self.resolution['x'] // ROUTRER_X_RATIO
        height = self.resolution['y'] // ROUTRER_Y_RATIO
        return {'x': width, 'y': height}

if __name__ == '__main__':
    n = Router('D:\\pc shit\\Cisco Packet Tracer 8.0\\bin\\PacketTracer.exe')
    n.take_and_put(2)