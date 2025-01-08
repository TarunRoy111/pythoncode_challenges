#Using Lambda Functions with sorted() You can sort a list of dictionaries based on a specific key.

students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Charlie', 'grade': 90},
    {'name': 'Bob', 'grade': 80}
]
students.sort(key=lambda x:x['grade'])
print(students)


#Reducing a List Using reduce() with a lambda function to compute the product of a list.
from functools import reduce
numbers = [1, 2, 3, 4]
a=reduce(lambda x,y:x+y,numbers)
print(a)
