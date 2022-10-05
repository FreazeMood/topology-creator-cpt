from main_api import Window
import pyautogui as pya

class Interface(Window):

    def __init__(self, directory) -> None:
        super().__init__(directory)
        self.current_position = self.find_mouse_pos()

    def find_mouse_pos(self) -> 'Point':
        position = pya.position()
        x,y = position.x, position.y 
        self.current_position = {'x': x, 'y': y}
        print(f'current mouse position: {self.current_position}')
        return self.current_position

    def find_icon_location(self, x_ratio, y_ratio) -> 'Point':
        width = self.resolution['x'] // x_ratio
        height = self.resolution['y'] // y_ratio
        return {'x': width, 'y': height}

    def take_and_put(self):
    
        if self.check_if_window_on_screen():
            self.define_screen_size()
            self.find_mouse_pos()

        else:
            raise TypeError
