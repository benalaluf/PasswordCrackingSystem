from src.connections.server import Server
from src.modules.client_manangment.handle_clients_select import HandleClientConnect

if __name__ == "__main__":
    server = HandleClientConnect(('localhost', 12345))
    server.start_server()