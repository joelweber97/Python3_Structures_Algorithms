#classes
class Cookie:
    def __init__(self, color):
        self.color = color


    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color



c1 = Cookie('blue')
print(c1.color)

c2 = Cookie('green')
print(c2.color)

print(c1.get_color())
print(c2.get_color())

c1.set_color('brown')
c2.set_color('yellow')
print(c1.get_color())
print(c2.get_color())


#pointers
num1 = 11
num2 = num1 #num2 points to the same 11 in memory

print(id(num1))
print(id(num2))

print(id(num1) == id(num2))

#so what happens if we set num2 to 22? what happens to num1

num2 = 22

print(num1, id(num1))
print(num2, id(num2))
#looks like num2 is now a seperate variable stored elsewhere
#in memory.

#ints are immutable so once it's stored in memory you cant
#change it


dict1 = {'value': 11}
dict2 = dict1
print(id(dict1), id(dict2))
#looks like dict2 is pointing to the same dict1 memory space

#dictionaries are mutable so we can change them in memory space 
#if we change the values of dict1 it will also change the
#values of dict2

dict2['value'] = 22
print(dict1, id(dict1), dict2, id(dict2))
#both still point to the same id, but that value of the dict
#has now changed for both variables


#now lets create a new variable
dict3 = {'value': 33}
dict2 = dict3   #these both now point to the same memory space


#if we set dict1 == dict2 now all 3 vars are pointing to the
#same dictionary in memory space
dict1 = dict2

print(id(dict1), id(dict2), id(dict3))
#now the original dictionary has no way of accessing
#the information in it so python deletes it using
#garbage collection.







