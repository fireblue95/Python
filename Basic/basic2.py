def CtoF():
	c = int(input("Input the Celsius:\n"))
	f = float(c * 1.8 + 32)
	print("%dC = %.1fF" % (c, f))

def main():
	CtoF()

if __name__ == "__main__":
	main()