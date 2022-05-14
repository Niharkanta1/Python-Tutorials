# first app
# Comment
print('Hello World!')
print('O----')
print(' ||||')
print('*' * 10)  # Expression

print('------------------------------------')
# Variables
price = 10
rating = 4.9
name = 'nihar'
is_published = False
print(price)

print('------------------------------------')
# Receiving Input
name = input('what is your name? ')
color = input('What is Favorite color? ')
print('Hi ' + name + '. Your favorite color ' + color)

print('------------------------------------')
# Type conversion
birth_year = input('Birth year: ')
print(type(birth_year))
age = 2022 - int(birth_year)
print(type(age))
print(age)

print('------------------------------------')
# String
course = "Python's for Beginners"
course2 = 'Python for "Beginners"'
course3 = '''
Hi Nihar
Here is our first email to you

thanks for the support
'''
print(course)
print(course2)
print(course3)
print(course[0])  # start index is form 0
print(course[-1])  # start from the end
print(course[0:3])  # substring
print(course[:])  # copy content of course

print('------------------------------------')
# Formatted String
first = 'nihar'
last = 'tripathy'

message = first + '[' + last + '] is a coder'
print(message)
msg = f'{first} [{last}] is a coder'

print('------------------------------------')
# String methods
course = "Python's for Beginners"
print(len(course))
print(course.upper())  # returns a copy
print(course.lower())
print(course.find('P'))  # returns first occurrance of P else -1
print(course.find('Beginners'))
print(course.replace('Beginners', 'Absolute Beginner'))
print('Python' in course)  # print true
