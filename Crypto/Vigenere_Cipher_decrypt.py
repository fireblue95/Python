def Vigenere_Cipher_decrypt(result_num, key_num):
	content = list()
	count = 0
	for i in range(len(result_num)):
		if(result_num[i] >= 65 and result_num[i] <= 90):
			if(result_num[i] < key_num[count]):
				content.append(chr(result_num[i] - 64 + 91 - key_num[count] + 64))
				count += 1
			else:
				content.append(chr(result_num[i] - key_num[count] + 65))
				count += 1
		else:
			content.append(chr(result_num[i]))
	return content
def main():
	result = input("Input the Content:\n")
	key_before = input("Input the Key:\n")
	length = ""
	key = ""
	for i in key_before.upper():
		if(ord(i) >= 65 and ord(i) <= 90):
			key += i
	for i in result.upper():
		if(ord(i) >= 65 and ord(i) <= 90):
			length += i
	if(len(length) > len(key)):
		count = 0
		for i in range(len(length)):
			if(i >= len(key)):
				key = key + key[count]
				count += 1
	key_num = list()
	result_num = list()
	for i in range(len(key)):
		key_num.append(ord(key[i].upper()))
	for i in range(len(result)):
		result_num.append(ord(result[i].upper()))
	content_result = "".join(Vigenere_Cipher_decrypt(result_num, key_num))
	if(result.isupper()):
		print(content_result.upper())
	else:
		print(content_result.lower())
if __name__ == "__main__":
	main()