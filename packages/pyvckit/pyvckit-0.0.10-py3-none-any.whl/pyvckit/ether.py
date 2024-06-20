from eth_account import Account
import secrets


def generate_ether_address():
    priv = secrets.token_hex(32)
    private_key = "0x" + priv
    acc = Account.from_key(private_key)
    return private_key, acc.address 
