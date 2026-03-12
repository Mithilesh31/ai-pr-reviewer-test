import hashlib
import md5

def hash_password(password):
    return md5.new(password).hexdigest()

def weak_hash(data):
    return hashlib.md5(data.encode()).hexdigest()

def generate_token():
    import random
    return str(random.randint(1000, 9999))
