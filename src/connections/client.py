from socket import socket, AF_INET, SOCK_STREAM

from src.modules.protocols.general import GeneralPacketType
from src.modules.protocols.protocol import HandelPacket, Packet, PacketType, SendPacket


class Client:

    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port
        self.addr = (self.server_ip, self.server_port)
        self.victim = socket(AF_INET, SOCK_STREAM)
        self.connected = True
        self.is_attacking = False

    def main(self):
        self.__connect()
        while self.connected:
            packet = HandelPacket.recv_packet(self.victim)
            self.handle(packet)

            if self.is_attacking:
                packet = Packet(PacketType.FOUND_PASSWORD, payload="iloveniggers".encode())
                SendPacket.send_packet(self.victim, packet)

    def handle(self, packet: Packet):
        print("got packet")
        if packet.packet_type == PacketType.START_ATTACK:
            self.is_attacking = True
            print("start attack")


    def __connect(self):
        print(f'connecting to {self.addr}')
        self.victim.connect(self.addr)
        packet = Packet(PacketType.FOUND_PASSWORD, "iloveniggers".encode())
        SendPacket.send_packet(self.victim, packet)

    def __on_connect(self, conn, addr):
        pass

    def __start_dict_attack(self):
        pass
