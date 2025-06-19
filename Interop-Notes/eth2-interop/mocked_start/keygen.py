from py_ecc.bls.api import privtopub
from hashlib import sha256 as _sha256
from typing import List, Dict
from ruamel.yaml import YAML
from eth_utils import (
    encode_hex,
    int_to_big_endian,
)

CURVE_ORDER = 52435875175126190479447740508185965837690552500527637822603658699938581184513


def int_to_hex(n: int, byte_length: int = None) -> str:
    byte_value = int_to_big_endian(n)
    if byte_length:
        byte_value = byte_value.rjust(byte_length, b'\x00')
    return encode_hex(byte_value)


def sha256(x):
    return _sha256(x).digest()


def generate_validator_keypairs(N: int) -> List[Dict]:
    keypairs = []
    for index in range(N):
        privkey = int.from_bytes(
            sha256(index.to_bytes(length=32, byteorder='little')),
            byteorder='little',
        ) % CURVE_ORDER
        keypairs.append({
            'privkey': int_to_hex(privkey),
            'pubkey': encode_hex(privtopub(privkey)),
        })
    return keypairs


if __name__ == '__main__':
    yaml = YAML(pure=True)
    yaml.default_flow_style = None

    keypairs = generate_validator_keypairs(10)
    with open('keygen_10_validators.yaml', 'w') as f:
        yaml.dump(keypairs, f)
