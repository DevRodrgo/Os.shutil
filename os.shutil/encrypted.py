import cryptography
from cryptography.fernet import Fernet
key = fernet.generate_key()

with open("secret.key", "wb") as key_file:
    key_file.write(key)

    print("key")

with open("shutil.py", "w") as shutil_python:
    shutil_python.open(shutil)

    print(shutil)

def load_key():

    """""""
    load previous generated key
    """""""

    return open("secret.key", "rb").read()

def load_file():
    return open("shutil.py", "rb").read()

def encrypt_file():
    "encrypt file"

    key = load_key()
    encoded_message = file.encode()
    f = Fernet(key)
    encrypt_file = f.encrypt(encode_file
    )

    print(encode_file)

if __name__ == "__main__":
    encrypt_file(os.path("/home/oem/Downloads/portifolio/js/shutil.py"))
    