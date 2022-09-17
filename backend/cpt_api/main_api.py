from fileinput import filename
import os
import psutil


class Cisco_Packet_Tracer:

    def __init__(self, directory) -> None:
        self.directory = directory
        self.is_opened = self.open_window(directory)
        print(f'''===============window opened successfully==================
window in opened state: {self.is_opened}''')

    def open_window(self, directory):
        os.chdir('D:')

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
        print(f'window resolution: {self.resolution}')

    def define_screen_size(self, directory):

        if self.is_opened:

            return 'resolution'


if __name__ == '__main__':
    cpt = Screen('D:\\pc shit\\Cisco Packet Tracer 8.0\\bin\\PacketTracer.exe')
