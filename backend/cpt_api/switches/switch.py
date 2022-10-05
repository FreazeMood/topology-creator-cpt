import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from interface import Interface


class Switch(Interface):

    
    def __init__(self, directory) -> None:
        super().__init__(directory)
        self.switch_location = self.find_icon_location()


    def take_and_put(self, qty: int) -> None:
        super().take_and_put()
        

    def wire(self):
        super().wire()

    

if __name__ == '__main__':
    sw = Switch('D:\\pc shit\\Cisco Packet Tracer 8.0\\bin\\PacketTracer.exe')
    sw.take_and_put(3)