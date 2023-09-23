from src.modules.client_manangment.handle_clients import ClientConnectionHandler


class SlavePatrol:

    def __init__(self, _connected_clients):
        _connected_clients = ClientConnectionHandler.connected_clients
        pass

    def give_timeout(self, client):
        pass

    def ask_work_for_client(self, client):
        pass

    # this is an init function that runs at the start of the attack
    def start_cloack_for_working_clients(self):
        pass

    def get_cloack_for_client(self, client):
        pass

    # this is a function that runs every time a client gets a chunk
    def rest_cloack_for_client(self):
        pass