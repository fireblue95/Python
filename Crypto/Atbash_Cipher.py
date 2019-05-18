def Atbash_Cipher(content):
	key = "ZYXWVUTSRQPONMLKJIHGFEDCBA"
	content_result = list()
	for i in content:
		if(ord(i) >= 65 and ord(i) <= 90):
			content_result.append(key[ord(i) - 65])
		else:
			content_result.append(i)
	return content_result
def main():
	content = input("Input the Content:\n")
	content_result = "".join(Atbash_Cipher(content.upper()))
	if(content.isupper()):
		print(content_result.upper())
	else:
		print(content_result.lower())
if __name__== "__main__":
	main()