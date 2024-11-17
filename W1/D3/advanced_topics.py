my_books = {
  "title": "Harry Potter",
  "author": "JK Rowling",
}

for key, value in my_books.items():
    print(f'The key is {key} and the value is {value}')

#range() and enumerate()

odd_nums = list(range(1,20,2))
print(odd_nums)

even_nums = []
for i in range(1,20):
    if i%2 == 0:
        even_nums.append(i)
print(even_nums)

students = ['John', "Anna", "Cathe", 'Mark']

for index, name in enumerate(students):
    students[index] = f'Hello {name}'

print(students)
# students[1] = 'Hello Maria'

#ZIP

list1 = ['a', 'b', 'c']
list2 = [1,2,3]

list3 = list(zip(list1, list2))
print(list3)

#break
#continue
#pass

# total_family =[]
# while True:
#     family_member = input('gimme the age, type "quit" when you are done')
#     if family_member == 'quit':
#         break
#     total_family.append(family_member)

# print(total_family)

#continue : the loop will go to the next iteration
for each_student in students:
    
    if each_student == 'Hello Cathe':
        continue
    else:
        print(f'{each_student}, how are you')

#pass
if students[0] is 'Hello Harry':
    pass #a developer keyword to help to structure the code before you have the logics
else:
    print('not Harry') 
        
#list comprehension
even_nums = []
for i in range(1,20):
    if i%2 == 0:
        even_nums.append(i)
print(even_nums)

even_nums =[i for i in range(1,20) if i%2 == 1]

even_nums =(i for i in range(1,20) if i%2 == 1)
print(type(set(even_nums)))

#dict comprehension
family_age = {'Lea': 12, 'Mark': 25, 'George': 50}
new_ages = {name:age + 1 for (name,age) in family_age.items()}
print(new_ages)