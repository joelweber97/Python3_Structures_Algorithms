#O(n)
def print_items(n):
    for i in range(n):
        print(i)
print_items(10) 

#drop constants
#O(n)
def print_items(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)
print_items(10)
#although this would technically be O(2n) since every n would 
#result in 2 processes but we drop the constant so it would
#still be O(n)

#O(n^2)
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
print_items(10)
#this results in n*n processes resulting in O(n^2)


#drop non-dominants
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
    for k in range(n):
        print(k)
print_items(10)
#as n increases the '+n' starts to mean less and less.
#therefore we can actually drop the '+n' and we just left with
#O(n^2)


#O(1)
def add_items(n):
    return n+n
add_items(100)
#Regardless of the size of n, there is only 1 operation.
#this is called constant time since the number of operations is constant



#O(log n)
# whats the most efficient way to find a number in a sorted list?
#1,2,3,4,5,6,7,8
#cut it in half and see if its in the first or second half
#do this again and again until we find the number we're looking for.
#for a list length 8 it only takes 8 operations to find that number
#2^3 = 8 which is the same as log sub2 of 8 = 3
#basically means how many times do we divide 8 by 2 to get a single number
#this works really well with really large numbers
#for instance, log sub2 1073741824 would only take 31 iterations to find a number.


#different terms for inputs
def print_items(a, b):
    for i in range(a):
        print(i)
    for j in range(b):
        print(j)
#this would simplify to O(a+b)
#whereas a nested loop
def print_items(a,b):
    for i in range(a):
        for j in range(b):
            print(i,j)
#would simplify to O(a*b)