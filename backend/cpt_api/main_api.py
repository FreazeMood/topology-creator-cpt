import os


class Screen:

    def __init__(self) -> None:

        self.resolution = self.define_screen_size()

    def define_screen_size(self):
        return 'resolution'


class Cisco_Packet_Tracer(Screen):

    def __init__(self, connection) -> None:
        super().__init__()
        self.is_opened = self.make_conn(connection)
        self.window = self.get_window()

    def make_conn(self, dir) -> 'connection':
        os.chdir('D:')

        try:
            os.startfile(dir)
            return True

        except FileNotFoundError as e:
            print(
                '===============issue with the path check if its correct================')
            raise e

    def get_window(self):

        if not self.is_opened:
            raise TypeError

        print('===============window opened successfully==================')
        print(self.resolution)


if __name__ == '__main__':
    cpt = Cisco_Packet_Tracer(
        'D:\\pc shit\\Cisco Packet Tracer 8.0\\bin\\PacketTracer.exe')
    print(f"window in opened state:\n{cpt.is_opened}")
