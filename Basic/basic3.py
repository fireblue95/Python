def years():
	year = int(input("Input the years:\n"))
	leap_year = (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
	print(leap_year)

def main():
	years()

if __name__ == "__main__":
	main()