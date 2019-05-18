def caesar_auto(content):
	for k in range(1,27):
		content_result = list()
		for i in content.upper():
			if(ord(i) >= 65 and ord(i) <= 90):
				if((ord(i) + k) > 90):
					content_result.append(chr((ord(i) - 65 + k) % 26 + 65))
				else:
					content_result.append(chr(ord(i) + k))
			else:
				content_result.append(i)
		content_result = "".join(content_result)
		if(content.isupper()):
			print("%02d" % k, ". ", content_result.upper())
		else:
			print("%02d" % k, ". ", content_result.lower())
def main():
	content = input("Input the Content:\n")
	caesar_auto(content)
if __name__ == "__main__":
	main()