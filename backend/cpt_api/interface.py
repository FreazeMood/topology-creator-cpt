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
