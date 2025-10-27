import hmac # hash-based message authentificaiton code
import hashlib

def calculate_hash(key: str, message:str ):
    b_key = key.encode()
    b_message = message.encode()
    hash_value = hmac.new(b_key, b_message, hashlib.sha256) #generates hash based message authentification code, requires the message, key, and hash method
    return hash_value.hexdigest()

key = "123456789"
hash1 = calculate_hash(key, "Pay me $100")
hash2 = calculate_hash(key, "Pay me $1000")
hash3 = calculate_hash(key, "Pay me $100")

print(hash1 == hash2)
print(hash1 == hash3)

# TODO
# create two functions
# def send_message(message_text) -> dict:
# {"text": ..., "hash": hash_value}


# def receive_message(message: dict)
# Verify if the hash is valid for the message sent