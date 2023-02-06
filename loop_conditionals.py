import names
import random
list_of_names = []
for i in range(random.randrange(20)):
    list_of_names.append(names.get_first_name())
names_lengths = [len(name) for name in list_of_names if len(name) > 5]
print(names_lengths)
n_N_names = [print(name) for name in list_of_names if 'n' in name or 'N' in name]
print(list_of_names)
while len(list_of_names) > 0:
    list_of_names.pop()
print(list_of_names)
