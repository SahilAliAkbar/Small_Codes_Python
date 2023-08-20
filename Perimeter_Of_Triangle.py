a = int(input('Enter first side: '))
b = int(input('Enter second side: '))
c = int(input('Enter third side: '))

def perimeter():

    # Calculate the perimeter
    perim = a + b + c

    return perim

perim = perimeter()
print( 'Perimeter is: ', format(perim,',.1f'))