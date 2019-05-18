def crypto(content_num, key_num):
	result = list()
	for i in range(len(content_num)):
		if(content_num[i] + key_num[i] > 90):
			result.append(chr((content_num[i] + key_num[i]) % 91 + 65))
		else:
			result.append(chr(content_num[i] + key_num[i]))
	return result
def main():	
	content = input("Input the Content:\n")
	key = input("Input the Key:\n")
	key_num = list()
	content_num = list()
	print(content)
	print(key)
	for i in range(len(key)):
		key_num.append(ord(key[i].upper()) - 65)
		content_num.append(ord(content[i].upper()))
	end = "".join(crypto(content_num, key_num))
	print(end.upper() if content.isupper() else end.lower())
if __name__ == "__main__":
	main()