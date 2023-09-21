from src.modules.cracking.generic_dict_attack import GenericDictAttack
import hashlib


class MD5DictAttack(GenericDictAttack):
    def _hash(self, text: str):
        return hashlib.md5(text.encode()).hexdigest()
    