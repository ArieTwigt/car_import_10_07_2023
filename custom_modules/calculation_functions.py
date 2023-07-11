import math


def calc_pythagoras(a, b, rounded=True, decimals=2):
    '''
    Function that applies the Pythagoras theorem

    Inputs:
    Required/postional arguments
    - a: a side of the triangle
    - b: b side of the triangle

    Default arguments
    - rounded: specify if value shoulde rounded
    - decimals: indicate number of decimals

    '''
    c_sqrd = math.pow(a, 2) + math.pow(b, 2)
    c = math.sqrt(c_sqrd)

    
    if rounded:
        c_rounded = round(c, decimals)
        return c_rounded
    else:
        return c