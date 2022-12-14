import os
import psutil
import platform
import pyautogui as pya
from constants import PATH_ERROR
import time



class Cisco_Packet_Tracer:

    def __init__(self, directory) -> None:
        self.directory = directory # the executable file of the packet tracer
        self.os = self.get_os()
        self.is_opened = self.open_window(directory) # check if the application is running else start it
        print(f'''===============Application successfully started==================
window in opened state: {self.is_opened}
current os is: {self.os}
''')

    win_os_names = ('Windows', 'win32', 'cygwin')
    mac_os_names = ('Mac', 'Darwin', 'Os2', 'Os2emx')

    def open_window(self, directory):

        if self.os in self.win_os_names:  # adaptation for windows
            # check if the current directory is the directory where's the program
            if os.getcwd()[0] != self.directory[0]:
                print(f"changing directory to: {self.directory[0:2]}")
                os.chdir(self.directory[0:2])

            try:
                if not self.packet_tracer_is_running():
                    os.startfile(directory)
                    return True

                return True

            except FileNotFoundError as e:
                print(PATH_ERROR)
                raise e

        if self.os in self.mac_os_names:  # adaptation for macOS
            # @TODO:
            #       raise a file not found error if os.system wasnt executed
            try:
                if not self.packet_tracer_is_running():
                    app = self.directory.split('/')[-1]
                    os.system(f"open -a '{app}'")
                    return True

                return True

            except FileNotFoundError as e:
                print(PATH_ERROR)
                raise e

    def get_os(self):
        return platform.uname().system

    def packet_tracer_is_running(self) -> bool:
        """ 
        check if there is a proccess with the needed name
        """
        file_name = self.directory.split('\\')[-1]
        return file_name in (p.name() for p in psutil.process_iter())


class Window(Cisco_Packet_Tracer):

    def __init__(self, directory) -> None:
        super().__init__(directory)
        self.window_on_screen = self.check_if_window_on_screen()
        print(f'cisco-packet-tracer is opened: {self.window_on_screen}')
        self.resolution = self.define_screen_size()
        print(f'screen resolution is: {self.resolution}')
        self.window_resolution = self.find_window_resolution()

    def define_screen_size(self):
        
        """
        returns the resolution of the main screen
        """
        
        return f'{pya.size().width} * {pya.size().height}'

    def check_if_window_on_screen(self) -> bool:
       
        """
        checks if the window of the application is on the screen,
        if it's not tries to open the window on the screen.
        """

        if self.os in self.win_os_names and self.packet_tracer_is_running:

            import win32gui
            import ctypes
            foreground_window = win32gui.GetForegroundWindow()
            active_window_name = win32gui.GetWindowText(foreground_window)
            self.window = win32gui.FindWindow(None, 'Cisco Packet Tracer')

            if not active_window_name == 'Cisco Packet Tracer':
                user32 = ctypes.windll.user32
                user32.SetForegroundWindow(self.window)

                if user32.IsIconic(self.window):
                    user32.ShowWindow(self.window, 9)

                return True

            return True

    def find_window_resolution(self):

        """
        finds the resolution and the position of the application.
        (the window has to be opened to make this work)
        """

        if self.os in self.win_os_names:

            import win32gui
            import pywintypes
            try:
                rect = win32gui.GetWindowRect(self.window)
                x = rect[0]
                y = rect[1]
                w = rect[2] - x
                h = rect[3] - y
                print("The window is %s:" % win32gui.GetWindowText(self.window))
                print("\tLocation: (%d, %d)" % (x, y))
                print("\t    Size: (%d, %d)" % (w, h))
                return {"location": (x, y), "size": (w, h)}
            
            except pywintypes.error:
                time.sleep(3) # give 3 secs to launch
                self.check_if_window_on_screen() # basiclly runs again to check if the window has launched
                self.find_window_resolution() # try to find the position and size again


if __name__ == '__main__':
    cpt = Window('D:\\pc shit\\Cisco Packet Tracer 8.0\\bin\\PacketTracer.exe')
