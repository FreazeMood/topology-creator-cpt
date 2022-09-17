import os
import psutil


class Cisco_Packet_Tracer:

    def __init__(self, directory) -> None:
        self.directory = directory
        self.is_opened = self.open_window(directory)
        print(f'''===============window opened successfully==================
window in opened state: {self.is_opened}''')

    def open_window(self, directory):

        if os.getcwd()[0] != self.directory[0]: #  check if the current directory is the directory where's the program 
            print(f"changing directory to: {self.directory[0:2]}")
            os.chdir(self.directory[0:2])

        try:
            if not self.packet_tracer_is_running():
                os.startfile(directory)
                return True
            
            return True

        except FileNotFoundError as e:
            print(
                '===============issue with the path check if its correct================')
            raise e

    def packet_tracer_is_running(self):
        file_name = self.directory.split('\\')[-1]
        return file_name in (p.name() for p in psutil.process_iter())


class Screen(Cisco_Packet_Tracer):

    def __init__(self, directory) -> None:
        super().__init__(directory)
        self.resolution = self.define_screen_size(directory)
        self.window_on_screen = self.check_if_window_on_screen()
        print(f'window resolution: {self.resolution}')

    def define_screen_size(self, directory):

        if self.is_opened:

            return 'resolution'

    def check_if_window_on_screen(self):
        pass


if __name__ == '__main__':
    cpt = Screen('D:\\pc shit\\Cisco Packet Tracer 8.0\\bin\\PacketTracer.exe')
