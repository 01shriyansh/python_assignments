#find the volume of the sphere with diameter 12 cm.

import math                                                 # we required value of constant (pi)

def volume(radius):
	return (4/3)*math.pi*radius**3                           # volume of sphere is given by V=(4/3)*pi*(radius)^3


diameter=12.0                                               # converted it to float as volume could be in decimals.

radius=diameter/2											# we require the radius not diameter so diameter=2*radius.

vol=volume(radius)                                         # volume is the function defined to calculate the volume of the sphere,and take radius of sphere as parameter
vol=round(vol,2)										   # we have rounded the vol to 2 digits to make it less complex							

print("volume of sphere with diameter 12 cm is {} cm".format(vol))




