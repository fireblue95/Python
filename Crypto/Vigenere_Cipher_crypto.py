def Vigenere_Cipher_crypto(content_num, key_num):
	result = list()
	count = 0
	for i in range(len(content_num)):
		if(content_num[i] >= 65 and content_num[i] <= 90):
			if(content_num[i] + key_num[count] > 90):
				result.append(chr((content_num[i] + key_num[count]) % 91 + 65))
				count += 1
			else:
				result.append(chr(content_num[i] + key_num[count]))
				count += 1
		else:
			result.append(chr(content_num[i]))
	return result
def main():	
	content = input("Input the Content:\n")
	key = input("Input the Key:\n")
	length = ""
	for i in content.upper():
		if(ord(i) >= 65 and ord(i) <= 90):
			length += i
	if(len(length) > len(key)):
		count = 0
		for i in range(len(length)):
			if(i >= len(key)):
				key = key + key[count]
				count += 1
	key_num = list()
	content_num = list()
	for i in range(len(key)):
		key_num.append(ord(key[i].upper()) - 65)
	for i in range(len(content)):
		content_num.append(ord(content[i].upper()))
	content_result = "".join(Vigenere_Cipher_crypto(content_num, key_num))
	if(content.isupper()):
		print(content_result.upper())
	else:
		print(content_result.lower())
if __name__ == "__main__":
	main()