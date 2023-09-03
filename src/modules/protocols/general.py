from enum import Enum

from src.modules.protocols.protocol import Packet, PacketType, PacketConstants


class GeneralPacketType(Enum):
    CONNECT = 0
    ACK = 1
    HASH_TYPE = 2
    WORDS = 3
    PASSWORD = 4
    EXIT = 5


class GeneralPacket(Packet):
    def __init__(self, packet_sub_type: GeneralPacketType, payload: bytes = PacketConstants.NO_DATA):
        super().__init__(PacketType.GENERAL, packet_sub_type.value, payload)
