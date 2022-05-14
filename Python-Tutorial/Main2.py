import math  # import module

# Arithmatic Operations (+ - * /)
print(10 / 3)  # floating point division
print(10 // 3)  # int division
print(10 % 3)  # print reminder
print(10 ** 3)  # power operator

x = 10
x = x + 3  # print 13
x += 3  # print 13

print('------------------------------------')
# Math functions
x = 2.9
print(round(x))
print(abs(-2.9))
print(math.ceil(2.9))
print(math.floor(2.9))

print('------------------------------------')
# IF statement
is_hot = True
is_cold = False

if is_hot:
    print("Its a hot day")
elif is_cold:
    print("Its a cold day")
else:
    print("Its a lovely day")

print("Enjoy your day")

print('------------------------------------')
# Logical Operator - and / or / not
has_high_income = True
has_good_credit = True
has_criminal_record = False
if has_high_income and has_good_credit and not has_criminal_record:
    print("Eligible for loan")

print('------------------------------------')
# Comparison Operator - > / < / == / != / >= / <=
name = "Something"
print(len(name) >= 9)

print('------------------------------------')
# While loop
i = 1
while i <= 5:
    print(i)
    i += 1

print(f"Done. i = {i}")

print('------------------------------------')
# For loop
for item in 'Python':
    print(item)

print(" ")

for item in ['Python', 'Java', 'C#']:
    print(item)

print(" ")

for item in range(10):
    print(item)

print(" ")

for x in range(3):
    for y in range(3):
        print(f"({x}, {y})")
