from src.connections.client import Client
from src.modules.client_manangment.client_test import ClientTest

if __name__ == '__main__':
    ClientTest(('localhost', 12345)).main()
