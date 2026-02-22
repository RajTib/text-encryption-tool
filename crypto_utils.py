from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from Crypto.Protocol.KDF import PBKDF2
import base64
import json

# ---------------- AES ---------------- #
def generate_aes_key(password, salt):
    return PBKDF2(password, salt, dkLen=32, count=100000)

def aes_encrypt(plaintext, password):
    salt = get_random_bytes(16)
    key = generate_aes_key(password, salt)
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))

    data = {
        "salt": base64.b64encode(salt).decode(),
        "iv": base64.b64encode(cipher.iv).decode(),
        "ciphertext": base64.b64encode(ciphertext).decode()
    }

    return json.dumps(data)

def aes_decrypt(encrypted_json, password):
    data = json.loads(encrypted_json)

    salt = base64.b64decode(data["salt"])
    iv = base64.b64decode(data["iv"])
    ciphertext = base64.b64decode(data["ciphertext"])

    key = generate_aes_key(password, salt)
    cipher = AES.new(key, AES.MODE_CBC, iv)

    return unpad(cipher.decrypt(ciphertext), AES.block_size).decode()

# ---------------- RSA ---------------- #
def generate_rsa_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def rsa_encrypt(data, public_key):
    rsa_key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    encrypted = cipher.encrypt(data)
    return base64.b64encode(encrypted).decode()

def rsa_decrypt(encrypted_data, private_key):
    rsa_key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    decrypted = cipher.decrypt(base64.b64decode(encrypted_data))
    return decrypted
