import zlib, sys

def get_id(mac):
	mac = int(mac, 16).to_bytes(6, 'big')
	return checksum(mac, True)

def checksum(input, compression=False):

	v3 = zlib.crc32(input, 0xDEADBEEF)
	v4 = zlib.crc32(input, v3)
	v5 = zlib.crc32(input, v4)
	v6 = zlib.crc32(input, v5)
	v7 = zlib.crc32(input, v6)
	
	v8 = v4.to_bytes(4, 'little') + v5.to_bytes(4, 'little') + v6.to_bytes(4, 'little') + v7.to_bytes(4, 'little')
	
	if not compression:
		return v8.hex()
	
	v9 = bytearray(8)
	for i in range(8):
		v9[i] = v8[i] ^ v8[i + 8]
	
	ret = bytearray(4)
	for i in range(4):
		ret[i] = v9[i] ^ v9[i + 4]
	
	return ret.hex()
	
print(gen_id(sys.argv[1]))