import socket

import threading

from src.modules.client_manangment.client_data import ClientData
from src.modules.protocols.general import GeneralPacketType
from src.modules.protocols.protocol import HandelPacket, PacketType


class Server:

    # TODO split to modules!!!!!
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.addr = (ip, port)
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.addr)

        self.is_running = True
        self.is_attacking = False
        self.connected_clients = list()

    def main(self):
        threading.Thread(target=self.__start_listing).start()

        if self.is_running:
            self.__admin_input()

    def __start_listing(self):
        print(f'LISTENING... ({self.ip}:{self.port})')
        self.server.listen()
        try:
            while True:
                conn, addr = self.server.accept()
                threading.Thread(target=self.__on_new_client, args=(conn, addr)).start()

        except Exception as e:
            print(e)
            self.server.close()

    def __start_attack(self):
        print("starting attack!!!")
        self.__choose_wordlist()
        self.__show_connected_clients()
        self.__handle_all_clients()
        self.__split_wordlist()

    def __on_new_client(self, conn, addr):
        self.connected_clients.append(ClientData(conn, addr))

    def __handle(self, conn: socket.socket):
        packet = HandelPacket.recv_packet(conn)

        if packet.packet_type == PacketType.GENERAL.value:
            if packet.packet_sub_type == GeneralPacketType.PASSWORD:
                print(f"password is: {packet.payload.decode()}")
                self.is_attacking = False

    def __handle_all_clients(self):
        for client in self.connected_clients:
            threading.Thread(target=self.__handle(client.conn)).start()

    def __admin_input(self):
        while True:
            raw_command = input("server % ", )
            command_components = raw_command.split(' ')
            command = command_components[0]
            command_args = command_components[1:]

            if raw_command == "client.show":
                self.__show_connected_clients()

            if command == "attack":
                print("attacking")

            print('try client.show ;)')

    def __show_connected_clients(self):
        print('-' * 20)
        for i, client in enumerate(self.connected_clients, start=1):
            print(f'{i}. {client.addr}')
        print('-' * 20)

    def __split_wordlist(self):
        pass

    def __choose_wordlist(self):
        pass

    def __start_dict_attack(self):
        pass
