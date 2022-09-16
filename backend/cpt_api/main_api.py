import os
import subprocess

class Cisco_Packet_Tracer:

    def __init__(self, connection):

        self.connection = self.make_conn(connection)
        self.cursor = self.get_cursor()


    def make_conn(self, dir) -> 'connection':
        os.chdir('D:')
        subprocess.call([dir])


    def get_cursor(self):
        
        if not self.connection:
            raise TypeError

if __name__ == '__main__':
    cpt = Cisco_Packet_Tracer('D:\\pc shit\\Cisco Packet Tracer 8.0\\bin\\PacketTracer.exe')
    print(cpt.connection)