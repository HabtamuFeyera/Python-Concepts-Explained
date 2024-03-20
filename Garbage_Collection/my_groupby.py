from itertools import groupby

# use a function as key
def smaller_than_3(x):
    return x < 3

group_obj = groupby([1, 2, 3, 4], key=smaller_than_3)
for key, group in group_obj:
    print(key, list(group))

# or use a lamda expression, e.g. words with an 'i':
group_obj = groupby(["hi", "nice", "hello", "cool"], key=lambda x: "i" in x)
for key, group in group_obj:
    print(key, list(group))

persons = [{'name': 'Alex', 'age': 25}, {'name': 'Abebe', 'age': 35}, 
           {'name': 'Monet', 'age': 27}, {'name': 'Chala', 'age': 18}]

for key, group in groupby(persons, key=lambda x: x['age']):
    print(key, list(group))