#import hashlib
#from Crypto.Cipher import AES
#from Crypto.Util.Padding import pad


def xorEncrypt(data, key):
	l = len(key)
	keyAsInt = [x for x in map(ord, key)]
	return bytes(bytearray(((data[i] ^ keyAsInt[i % l]) for i in range(0, len(data)))))

def xorDecrypt(data, key):
	l = len(key)
	keyAsInt = [x for x in map(ord, key)]
	return bytes(bytearray(((data[i] ^ keyAsInt[i % l]) for i in range(0,len(data)))))


'''def aesEncrypt(data, key):
	iv = 16 * b'\x00'
	cipher = AES.new(hashlib.sha256(key).digest(), AES.MODE_CBC, iv)
	return cipher.encrypt(pad(data, AES.block_size))

def aesDecrypt(data, key):
	data = bytearray(b64decode(data))
	key = bytearray(b64decode(key))
	iv = 16 * b'\x00'
	cipher = AES.new(hashlib.sha256(key).digest(), AES.MODE_CBC, iv)
	return cipher.decrypt(pad(data, AES.block_size))'''