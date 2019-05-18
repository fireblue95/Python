def (content):
	return content_result
def main():
	content = input("Input the Content:\n")
	content_result = "".join((content.upper()))
	if(content.isupper()):
		print(content_result.upper())
	else:
		print(content_result.lower())
if __name__== "__main__":
	main()