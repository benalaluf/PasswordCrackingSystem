from socket import socket, AF_INET, SOCK_STREAM

from src.modules.protocols.general import GeneralPacketType
from src.modules.protocols.protocol import HandelPacket, Packet, PacketType


class Client:

    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port
        self.addr = (self.server_ip, self.server_port)
        self.victim = socket(AF_INET, SOCK_STREAM)
        self.connected = True

    def main(self):
        self.__connect()
        while self.connected:
            packet = HandelPacket.recv_packet(self.victim)
            self.handle(packet)

    def handle(self, packet: Packet):
        print("got packet")
        if packet.packet_type == PacketType.GENERAL.value:
            if packet.packet_sub_type == GeneralPacketType.WORDS:
                print("doing stuff")

    def __connect(self):
        print(f'connecting to {self.addr}')
        self.victim.connect(self.addr)

    def __on_connect(self, conn, addr):
        pass

    def __start_dict_attack(self):
        pass
