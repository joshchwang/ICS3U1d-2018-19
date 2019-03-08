import math

radius = int(input("Please input the radius: "))
height = int(input("Please input the height: "))
def cylinder(r, h):
    cyl = math.pi*r**2*h
    print(round(cyl, 1))

def cone(r, h):
    con = 1/3*math.pi*r**2*h
    print(round(con, 1))

def sphere(r):
    sph = 4/3*math.pi*r**3
    print(round(sph, 1))

# Call the main function to get the program started.
cylinder(radius, height)
cone(radius, height)
sphere(radius)