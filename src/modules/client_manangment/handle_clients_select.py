import select
import socket


class HandleClientConnections:

    def __init__(self, server_socket: socket.socket):
        self.server_socket = server_socket
        self.connected_clients = list()

    def start_listening(self):
        self.server_socket.listen(1)

    def on_new_client(self):
        pass

listen_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


if __name__ == '__main__':

client_sockets = []

try:
    while True:

        ready_to_read, ready_to_write, in_error = select.select(client_sockets + [listen_sock], [], [])

        for sock in ready_to_read:

            if sock == listen_sock:

                client_sock, client_address = listen_sock.accept()
                client_sockets.append(client_sock)
                print(f"New client: {client_address}")

                client_sock.sendall(welcome_msg.encode())

            else:

                client_msg = sock.recv(FLOW_CONTROL).decode()
                print(f"Client sent: {client_msg}")