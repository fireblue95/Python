import math
def circle_radius_perimeter():
	radius = float(input("Input the radius:\n"))
	perimeter = 2 * math.pi * radius
	area = radius ** 2 * math.pi
	print("Radius: %.2f" % radius)
	print("Perimeter: %.2f" % perimeter)
	print("Area: %.2f" % area)

def main():
	circle_radius_perimeter()

if __name__ == "__main__":
	main()