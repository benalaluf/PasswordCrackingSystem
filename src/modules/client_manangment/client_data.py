import random
from dataclasses import dataclass, field
import socket
from typing import ClassVar


@dataclass
class ClientData:
    client_id: int = field(init=False)
    conn: socket.socket = field(repr=False)
    addr: tuple

    client_ids: ClassVar[set] = field(repr=False, default=set())

    def __post_init__(self):
        self.victim_id = self.__generate_id()

    # purge
    def __generate_id(self):
        victim_id = random.randint(100,9999)
        if victim_id not in self.client_ids:
            ClientData.client_ids.add(victim_id)
            return victim_id
        else:
            return self.__generate_id()
