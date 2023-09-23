import socket
import threading

import select
import sys

from src.modules.client_manangment.client_data import ClientData
from src.modules.protocols.general import GeneralPacketType
from src.modules.protocols.protocol import HandelPacket, PacketType, Packet, SendPacket


class HandleClientConnect:

    connected_clients = list()

    def __init__(self, addr):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(addr)

    def accept_connection(self):
        conn, addr = self.server_socket.accept()
        HandleClientConnect.connected_clients.append(ClientData(conn, addr))
        print(f"New client: {addr}")

    def start_server(self):
        self.server_socket.listen()
        print("LISTENING...")
        while True:
            readable, _, _ = select.select([client.conn for client in HandleClientConnect.connected_clients] + [self.server_socket], [], [])
            self.__show_connected_clients()
            for client in readable:
                if client == self.server_socket:
                    self.accept_connection()

                else:
                    self.__handle(client)

    def __broadcast(self, sender_sock, packet):
        packet = Packet(PacketType.START_ATTACK)
        for client_sock in HandleClientConnect.connected_clients:
            if client_sock != sender_sock:
                SendPacket.send_packet(client_sock, packet)

    def __handle(self, conn):
        try:
            packet = HandelPacket.recv_packet(conn)
            # print(f"Data received from client: {packet.payload.decode()}")
            SendPacket.send_packet(conn, packet)

        except (ConnectionResetError, ConnectionAbortedError):
            self.connected_clients.remove(conn)
            print(f"A client disconnected")

    def __show_connected_clients(self):
        print('-' * 20)
        for i, client in enumerate(self.connected_clients, start=1):
            print(f'{i}. {client.addr}')
        print('-' * 20)

    def get_connected_clients(self):
        return self.connected_clients


if __name__ == "__main__":
    server = HandleClientConnect(('localhost', 12345))
    server.start_server()
