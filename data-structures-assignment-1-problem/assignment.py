# 1) Create a list of “person” dictionaries with a name, age and list of hobbies for each person. Fill in any data you want.
persons_info = [{'name': 'Serhii', 'age': 37, 'hobbies': ['programming', 'cooking', 'swimming'],}, {'name': 'Kuba', 'age': 46, 'hobbies': ['eating', 'drinking', 'joking'],}, {'name': 'Jan', 'age': 40, 'hobbies': ['walking', 'reading', 'running'],}]
print(persons_info)
# 2) Use a list comprehension to convert this list of persons into a list of names (of the persons).
list_names = [person['name'] for person in persons_info]
print(list_names)
# 3) Use a list comprehension to check whether all persons are older than 20.
older_persons = [person for person in persons_info if person['age'] > 20]
are_older = all([person['age'] > 20 for person in persons_info])
print(are_older)
if len(older_persons) == len(list_names):
    print(True)
else:
    print(False)
# 4) Copy the person list such that you can safely edit the name of the first person (without changing the original list).
# copied_persons = persons_info[:]
copied_persons = [person.copy() for person in persons_info]
copied_persons[0]['name'] = 'Inna'
print(copied_persons)
# 5) Unpack the persons of the original list into different variables and output these variables.
person_1, person_2, person_3 = persons_info
print('First person:\n', person_1, '\n', 'Second person:\n', person_2, '\n', 'Third person:\n', person_3, '\n')
