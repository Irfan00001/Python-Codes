import json
import requests
from Crypto.Cipher import AES
from base64 import b64encode,b64decode
from Crypto.Util.Padding import pad
from cryptography.hazmat.primitives import padding
from Crypto.Random import get_random_bytes

#iv=get_random_bytes(16)
iv=get_random_bytes(16)
data1="Kotak Mahindra Bank"
data=bytes(data1,'utf-8')
data=iv+data

key="asdfasdfasdfasdfasdfasdfasdfasdf" #32 Byte key Size
key=bytes(key,'utf-8')
print(key)

#data=cipher.encrypt(data)
cipher=AES.new(key,AES.MODE_CBC)
ct_bytes=cipher.encrypt(pad(data,AES.block_size))

iv = b64encode(cipher.iv).decode('utf-8')
ct = b64encode(ct_bytes).decode('utf-8')
result=json.dumps({"iv":iv,"ciphertext":ct})
print(result)
#Good
