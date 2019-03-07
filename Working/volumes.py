import math

r = int(input("Please input the radius"))
h = int(input("Please input the height"))
def cylinder(r, h):
    math.pi*r**2*h

def cone(r, h):
    1/3*math.pi*r**2*h

def sphere(r):
    4/3*math.pi*r**3

def main():
    print(cylinder(r, h))
    print(cone(r, h))
    print(sphere(r))

# Call the main function to get the program started.
main()