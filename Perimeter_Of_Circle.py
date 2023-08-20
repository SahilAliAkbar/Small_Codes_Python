from math import pi
def circum(r):
    return 2*pi*r
radius=float(input("Enter radius: "))
print(f"Circumference is {round(circum(radius),2)}")