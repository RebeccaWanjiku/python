# list datastructure
# list are mutable
# list are ordered
# list are indexed
from datatypes import student

fruits=['apples' , 'mangoes' , 'oranges' , 'pineapples' , 'banana' , 'pear' ]
fruits[0]= "Watermelon"
numbers=[1 ,2 ,3 ,4 ,5 ,6 ]
number2=[10 ,90 ,-70 ,8 ,76 ,-9 ,6,45 ]
number2 . sort(reverse=True)
print(number2)

print(fruits)
numbers . append(7)
print(numbers)
print(f"I love eating {fruits[3]}")
# tuple datastructures
# tuples are immutable/unchangeable
# tuples are ordered
# tuples are indexed
cars=('audi' ,'toyota' ,'mercedes' ,'honda')
print(cars)
nambari=(78,90,-6,-10 ,7,53,-85,9)
# cars range
print(cars)
# nambari.sort(reverse=True)
print(sorted(nambari))
# set datastructure
# set are unordered
# set are not indexed
# print(sorted())
computers={'hp' ,'dell' , 'lenovo' , 'ibm' ,'acer' }
computers .add('google')
computers.remove('lenovo')

print(computers)
num1={1 ,2 ,3}
num2={4,6,7}
union_set=num1.union(num2)
print(union_set)
# dictionaries datasructure
student={'Name' : 'John' , 'Age' :5, 'gender':'male','School':"University of Nairobi"}
print(student['Name'])
print(f"student name: {student['Name']}")
print(student['School'])
print(f"student school:{student['School']}")