def decrypt(result_num, key_num):
	content = list()
	for i in range(len(result_num)):
		if(result_num[i] < key_num[i]):
			content.append(chr(result_num[i] - 64 + 91 - key_num[i] + 64))
		else:
			content.append(chr(result_num[i] - key_num[i] + 65))
	return content
def main():
	result = input("Input the Content:\n")
	key = input("Input the Key:\n")
	key_num = list()
	result_num = list()
	print(result)
	print(key)
	for i in range(len(key)):
		key_num.append(ord(key[i].upper()))
		result_num.append(ord(result[i].upper()))
	end = "".join(decrypt(result_num, key_num))
	print(end.upper() if result.isupper() else end.lower())
if __name__ == "__main__":
	main()