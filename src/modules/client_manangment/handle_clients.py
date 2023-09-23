# TODO
import socket

from src.modules.client_manangment.client_data import ClientData
from src.modules.protocols.protocol import Packet, SendPacket


class ClientConnectionHandler:
    _connected_clients = list()

    def __init__(self, server_socket: socket.socket):
        self.server_socket = server_socket

    def listen_to_new_clients(self):
        pass

    def on_new_clients(self, client_data: ClientData):
        ClientConnectionHandler._connected_clients.append(client_data)

    def on_dissconnected_client(self, client_data: ClientData):
        ClientConnectionHandler._connected_clients.remove(client_data)

    def update_connected_clients(self):
        pass

    def check_if_client_connected(self):
        pass

    @property
    def connected_clients(self):
        return self._connected_clients


class ClientCommunicationHandler:

    def __init__(self):
        pass

    def send_to_client(self, client_data: ClientData, packet: Packet):
        client_socket = client_data.conn
        SendPacket.send_packet(client_socket, packet)


