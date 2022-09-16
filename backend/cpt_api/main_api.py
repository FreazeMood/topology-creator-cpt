

class Cisco_Packet_Tracer:

    def __init__(self, connection):

        self.connection = self.make_conn(connection)
        self.cursor = self.get_cursor()


    def make_conn(self, dest) -> 'connection':
        pass


    def get_cursor(self):
        
        if not self.connection:
            raise TypeError

