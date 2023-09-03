from src.connections.client import Client

if __name__ == '__main__':
    client = Client("localhost", 6968).main()
