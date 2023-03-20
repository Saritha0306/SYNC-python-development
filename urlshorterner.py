import hashlib
import string
import random
def shorten_url(url):
    salt = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))
    hash_object = hashlib.sha256((url + salt).encode())
    hex_dig = hash_object.hexdigest()[:8]
    return hex_dig
url = 'https://www.example.com/long-url'
short_url = shorten_url(url)
print(short_url)
