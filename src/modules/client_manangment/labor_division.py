from src.modules.client_manangment.client_data import ClientData
from src.modules.client_manangment.handle_clients import ClientCommunicationHandler
from src.modules.protocols.protocol import Packet, PacketType


class LaborDivision:

    def __init__(self, dict_path):
        self.dict_path = dict_path
        self.is_finished_labor = False
        self.read_file_genarator = self.read_file_in_chunks()
        self.handler = ClientCommunicationHandler()

    def get_password_chunk(self):
        chunk = next(self.read_file_genarator)
        if not chunk:
            pass
        else:
            return chunk

    def read_file_in_chunks(self, chunk_size=100):
        with open(self.dict_path, 'r') as file:
            lines = ''
            while True:
                for _ in range(chunk_size):
                    line = file.readline()
                    if not line:
                        break
                    lines += line
                if lines != '':
                    yield lines
                    lines = ''
                else:
                    yield None


    def give_words_to_client(self, client: ClientData):
        chunk = self.get_password_chunk()
        packet = Packet(PacketType.PASSWORD_CHUNK, payload=chunk.encode())
        self.handler.send_to_client(client, packet)



if __name__ == '__main__':
    labor = LaborDivision("/Users/blu/GitHub/PasswordCrackingSystem/src/modules/wordlists/8Digit.lst")


    print(labor.get_password_chunk())
    print('-'*20)
    print(labor.get_password_chunk())
    print('-'*20)
    print(labor.get_password_chunk())
    print('-'*20)
    print(labor.get_password_chunk())
    print('-'*20)
    print(labor.get_password_chunk())
    print('-'*20)
    print(labor.get_password_chunk())