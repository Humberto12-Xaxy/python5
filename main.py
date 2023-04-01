
def leap_year(year):

    if year % 400 == 0:
        return True

    elif year % 4 == 0 and year % 100 != 0:
        return True
    
    else: 
        return False
    


if __name__ == '__main__':

    if leap_year(2012):
        print('Es bisiesto')
    else:
        print('No es bisiesto')
