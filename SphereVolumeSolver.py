#This program takes a number from the user and prints out the volume of a sphere
#with a radius of that number
import math
def main():
    rad = float(input("Enter in a number: "))
    vol = (4/3)*math.pi*(rad**3)
    print("The volume of a sphere with the radius ", rad, " equals ",int(vol))
main()
