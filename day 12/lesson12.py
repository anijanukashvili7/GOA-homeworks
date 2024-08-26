name = str(input("please enter your name: "))
last_name = str(input("please enter your last_name: "))
age = int(input("please enter your age: "))
address = int(input('please enter your address: '))

your_information = [ ]

your_information.append(name)
your_information.append(last_name)
your_information.append(age)
your_information.append(address)

print(your_information)
print(your_information[0:2])
print(your_information[1:3])
print(your_information[0:3])
print(your_information[1:4])

# 2

num1 = int(input("please enter negative number: "))

negative_numbers = []

for i in range(num1,0):
    negative_numbers.append(i)

print(negative_numbers)

# 3

name = "ani"
last_name = "janukashvili"

about_you =["ani","janukashvili"]

print(about_you[0])
print(about_you[1])

# 4

movie = ["harry_potter","twilight","teen_wolf","the lord of the rings","The Chronicles of Narnia"]


print(movie)
print(movie[0:2])
print(movie[1:3])
print(movie[0:3])
print(movie[1:4])

# 5

academy_name = str(input("please enter academy_name: "))

if academy_name[0]== 'G' or academy_name[0]==  'g':
    print("GOA is the best choise!")
else:
    print("your opinion is wrong!")




































