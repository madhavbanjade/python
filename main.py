import math
import myModule
# print ('Enter a number:')
# num1 = input()
# print('Enter a number')
# num2  = input()
# result = int(num1) + int(num2)
# print('The answer is:', result)

# age = input('Enter your age: ')
# if int(age) <= 18:
#     print('You are under age for this place')
# elif int(age) >= 25:
#     print('You are over age for this place ') 
# else :
#     print("Congratulation, your visa is granted!")


# (not or and) are keywords
# x = 2 
# y = 3 
# if not(x == y and x + y == 5):
#     print('Run')
# else:
#     print(':)
# start stop and step
# for x in range(0, 10, 1):
#     print(x)

    # lists
# fruits = ['apple', 'strawberry', 'mango', 6]
# print(fruits)

# # add
# fruits.append('blueberry')
# print(fruits)

# # position
# fruits[1] = 4
# print(fruits)

# fruits[1:1] = "madhav"
# print(fruits)

# tuples
# fruits = ('mango', "apple", "banana", 4)
# print(type(fruits))

# for fruit in fruits:
#     print(fruit)

# slice methods [start: end : stop ]


    # string methods .strip() => remove space, len() => length, .lower/uppper, /split() => spits word ,
    #  len(text), .split('a')

# # functions
# def addTwo(x):
#     return x + 1
# number = addTwo(2)
# print(number)


# def accel (mass, force):
#     return mass * force

# acc = accel(2, 4)
# print(acc)

# reading form a text files
# file = open('file.txt', 'r')
# f = file.readlines()
# print(f)

# newlist = []
# for line in  f:
#  newlist.append(line.strip())
# print(newlist)

# writing to a file this means overwritting the whole file 
# file = open('file.txt', 'w') 
# f = file.write('iphone 11 \n')
# f = file.write('bedsheet')

# print(f)
# file.close()

# # .find and .count in string not other langauges includes this 
# fruits = "mangokbihhlihbwihbihhbweiebifhwbihfbqihbhpibvpiqwba"
# print(fruits.count("b"))

# introduction to moduler program


print(math.pi)
print(myModule.func(1))