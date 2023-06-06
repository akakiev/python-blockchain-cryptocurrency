# 1) Import the random function and generate both a random number between 0 and 1 as well as a random number between 1 and 10.
import random as rd
import datetime as dt
random_number_float = rd.random()
random_number_integer = rd.randint(1, 10)
print(f'{random_number_float:.2f}')
print(random_number_integer)
# 2) Use the datetime library together with the random number to generate a random, unique value.
random_unique_value = dt.datetime.now().strftime('%Y%m-%d%H-%M%S-') + str(random_number_integer)
print(random_unique_value)
