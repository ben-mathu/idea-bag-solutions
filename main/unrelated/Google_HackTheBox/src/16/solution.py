import hashlib

hash_obj = hashlib.md5(b'gctfHello')
hash_obj2 = hashlib.md5(b'gctfCTF')
print(hash_obj.hexdigest())
print(hash_obj2.hexdigest())