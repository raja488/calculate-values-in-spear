#V = 4/3 π r³
#calculating volume of a sphere 
import math
def get_volume(rad):
    volume=(4/3)*math.pi*(rad**3)
    return volume

def get_area(rad):
    area=4*math.pi*(rad**2)
    return area

def get_diameter(rad):
    diameter=2*rad
    return diameter

def get_radius():
    diameter=2*rad
    radius=(diameter/2)
    return radius
def get_circumference(rad):
    diameter=2*rad
    radius=(diameter/2)
    circum=2*math.pi*rad
    return circum

    



rad=int(input("enter the radius of the sphere "))
volume=get_volume(rad)
print(volume)
area=get_area(rad)
print(area)
diameter=get_diameter(rad)
print(diameter)
radius=get_radius()
print(radius)
circum=get_circumference(rad)
print(circum)














    
    


