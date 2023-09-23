import socket
import threading
import time

from src.modules.protocols.protocol import *


class ClientTest:


    def __init__(self, addr):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(addr)


    def main(self):
        packet = Packet(PacketType.MSG, payload='hello'.encode())
        threading.Thread(target=self.handle).start()
        while True:
            SendPacket.send_packet(self.client_socket, packet)
            
    def handle(self):
        while True:
            packet = HandelPacket.recv_packet(self.client_socket)
            print(packet.payload.decode())
        
        
if __name__ == '__main__':
    if __name__ == '__main__':
        ClientTest(('localhost', 12345)).main()
