my_name = "Serhii"
my_age = 37

def personal_data():
    '''Prints my data as one string.'''
    print(my_name + ' '+ str(my_age))

personal_data()


def first_and_last_name(name, surname):
    '''Prints first and last names as one string.
    
    Arguments:
        :name: the first name of the person.
        :surname: the last name of the person.
    '''
    print(name + ' ' + surname)

first_and_last_name('Serhii', 'Baraban')


def lived_decades(age):
    '''Calculates and returns the number of decades you already lived.
    
    Argument:
        :age: the age of the person.
    '''
    number_decades = age // 10
    return number_decades

print(lived_decades(my_age))