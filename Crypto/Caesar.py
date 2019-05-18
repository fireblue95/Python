def caesar_crypto(content, key):
	content_result = list()
	for i in content.upper():
		if(ord(i) >= 65 and ord(i) <= 90):
			if((ord(i) + key) > 90):
				content_result.append(chr((ord(i) - 65 + key) % 26 + 65))
			else:
				content_result.append(chr(ord(i) + key))
		else:
			content_result.append(i)
	content_result = "".join(content_result)
	if(content.islower()):
		print(content_result.lower())
	else:
		print(content_result.upper())
def caesar_decrypt(content, key):
	content_result = list()
	for i in content.upper():
		if(ord(i) >= 65 and ord(i) <= 90):
			if((ord(i) - key) < 65):
				content_result.append(chr((ord(i) - 65 -key) % 26 + 65))
			else:
				content_result.append(chr(ord(i) - key))
		else:
			content_result.append(i)
	content_result = "".join(content_result)
	if(content.isupper()):
		print(content_result.upper())
	else:
		print(content_result.lower())
def main():
	content = input("Input the Content:\n")
	key = int(input("Input the key:\n")) % 26
	choice = input('Encrypt or Decrypt:(en or de)\n')
	if (choice[:2] == "en"):
		caesar_crypto(content, key)
	elif(choice[:2] == "de"):
		caesar_decrypt(content, key)
if __name__ == "__main__":
	main()