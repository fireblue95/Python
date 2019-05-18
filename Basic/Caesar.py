def caesar():
	choice = input('Do you want to encrypt or decrypt:\n')
	if (choice == 'en'):
		encrypt = input('Input the string:').lower()
		print(encrypt)
		key = int(input('Input the key:\n')) % 26
		print(key)
		encrypt_result = list()
		for i in encrypt:
			if(ord(i) >= 97 and ord(i) <= 122):
				if(ord(i) + key > 122):
					encrypt_result.append(chr((ord(i) - 97 + key) % 26 + 97))
				else:
					encrypt_result.append(chr(ord(i) + key))
		encrypt_result = "".join(encrypt_result)
		print(encrypt_result)
	elif(choice == 'de'):
		encrypt = input('Input the string:').lower()
		print(encrypt)
		key = int(input('Input the key:\n')) % 26
		print(key)
		encrypt_result = list()
		for i in encrypt:
			if(ord(i) >= 97 and ord(i) <= 122):
				if(ord(i) - key < 97):
					encrypt_result.append(chr((ord(i) - 97 -key) % 26 + 97))
				else:
					encrypt_result.append(chr(ord(i) - key))
		encrypt_result = "".join(encrypt_result)
		print(encrypt_result)
def main():
	caesar()
if __name__ == "__main__":
	main()