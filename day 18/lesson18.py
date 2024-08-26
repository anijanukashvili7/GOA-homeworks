#  1

user_name = (input("please enter your name: "))

if user_name == user_name.upper():
    print("yes!")
else:
    pass

#  2

user_word = input("please enter uppercase word: ")

count = 1

for char in user_word:
    count = count + 1
if char.lower() in user_word:
    user_word = input("please enter uppercase word: ")

print(count, user_word)

#  3

user_name = input("please enter your name: ")

def my_find(value_to_find):
    for index in range (len("user_name.index")):
        if user_name.index % 2 == 0:
            return(user_name.index.upper())
        else:
            return(user_name.index.lower())




































