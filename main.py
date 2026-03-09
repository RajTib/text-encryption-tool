from crypto_utils import *
import base64

# ---------------------------------------------------------------------------------------------------------- #

# For Encrypting the given message and password
def hybrid_encrypt(message, password):
    # AES encrypt message
    aes_encrypted = aes_encrypt(message, password)

    # Generate RSA keys
    private_key, public_key = generate_rsa_keys()

    # Add the public key to a file
    with open("public.pem", "wb") as f:
        f.write(public_key)

    # Add the private key to a file
    with open("private.pem", "wb") as f:
        f.write(private_key)

    # Encrypt password using RSA
    encrypted_password = rsa_encrypt(password.encode(), public_key)

    print("\n--- ENCRYPTED DATA ---")
    print("AES Encrypted Message:", aes_encrypted)
    print("RSA Encrypted Password:", encrypted_password)

    return private_key, aes_encrypted, encrypted_password

# ---------------------------------------------------------------------------------------------------------- #

# For decrypting the given key, data and encrypted password
def hybrid_decrypt(private_key, aes_data, encrypted_password):
    # Decrypt password
    password = rsa_decrypt(encrypted_password, private_key).decode()

    # Decrypt AES data
    decrypted_message = aes_decrypt(aes_data, password)

    print("\n--- DECRYPTED MESSAGE ---")
    print(decrypted_message)

# ---------------------------------------------------------------------------------------------------------- #

# Main executable loop
if __name__ == "__main__":
    print("1. Encrypt")
    print("2. Decrypt")
    choice = input("Choose option: ")

    if choice == "1":
        msg = input("Enter message: ")
        password = input("Enter password: ")
        private_key, aes_data, enc_pass = hybrid_encrypt(msg, password)

        print("\nSAVE THIS PRIVATE KEY SAFELY:")
        print(private_key.decode())

    elif choice == "2":
        aes_data = input("Paste AES Encrypted Message: ")
        enc_pass = input("Paste RSA Encrypted Password: ")

        with open("private.pem", "rb") as f:
            private_key = f.read()

        hybrid_decrypt(private_key, aes_data, enc_pass)
