# FILE ENCRYPTION WITH AES METHOD
from cryptography.fernet import Fernet

# FUNCTION FOR LOADING KEY
def load_key():
    # Loads the key from the current directory named `key.key`
    return open("key.key", "rb").read()

# FUNCTION FOR KEY GENERATION
def generate_key():
    key = Fernet.generate_key()
    # error handling for key generation
    try:
        with open('key.key', 'wb') as mykey:
            mykey.write(key)
    except:
        print("Error in Key Generation!\nPlease Try Again\n")
        quit()

# FUNCTION FOR ENCRYPTION
def encryption():
    # handling for key loading
    try:
        key = load_key()
    except:
        print("No Key Found!\nPlease Generate Key\n")
        quit()

    f = Fernet(key)

    name = input('Enter File Name: ')
    # handling for filename
    try:
        with open(name, 'rb') as original_file:
            original = original_file.read()
    except:
        print("No File Found!\n")
        quit()

    encrypted = f.encrypt(original)

    with open ('enc_'+name, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

# FUNCTION FOR DECRYPTION
def decryption():
    # handling for key
    try:
        key = load_key()
    except:
        print("No Key Found!\nPlease Provide Decryption Key\n")
        quit()

    f = Fernet(key)

    name = input('Enter File Name: ')
    # handling for filename
    try:
        with open(name, 'rb') as encrypted_file:
            encrypted = encrypted_file.read()
        name = name[4:]
    except:
        print("No File Found!\n")
        quit()
    
    # handling for invalid key provided
    try:
        decrypted = f.decrypt(encrypted)
    except:
        print("Invalid Key!\nPlease Provide Correct Key\n")
        quit()

    with open('dec_'+name, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)


# MAIN BODY
task = input("Key Generation (K), Encryption (E), Decryption (D): ").lower()

if task == 'k':
    generate_key()
    print("Key Generated Successfully!\n")

elif task == 'e':
    encryption()
    print("File Encrypted Successfully!\n")

elif task == 'd':
    decryption()
    print("File Decrypted Successfully!\n")

else:
    print("Invalid Option!\n")
    quit()

# *********** SCRIPT ENDS HERE ***********