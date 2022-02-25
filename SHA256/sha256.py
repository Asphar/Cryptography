import hashlib

def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

print("Enter the message you want to be encrypted : ")
hash_string = str(input())

hash_signature = encrypt_string(hash_string)

print(hash_signature)
