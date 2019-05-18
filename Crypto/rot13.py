def rot13(content_num):
	result = list()
	for i in range(len(content_num)):
		if(content_num[i] > 64 and content_num[i] < 78):
			result.append(chr(content_num[i] - 65 + 78))
		elif(content_num[i] > 77 and content_num[i] < 91):
			result.append(chr(content_num[i] - 78 + 65))
		else:
			result.append(chr(content_num[i]))
	return result
def main():
	content = input("Input the Content:\n")
	content_num = list()
	for i in range(len(content)):
		content_num.append(ord(content[i].upper()))
	end = "".join(rot13(content_num))
	print(end.lower())
if __name__ == "__main__":
	main()