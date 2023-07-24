

#init, append, prepend, and insert all are responsible
#for creating new nodes. To avoid writing a node creation
#code in each of the methods we can create a single
#node class and init method to create a new node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next



    def append(self, value):
        '''
            # append to end of linked list
            # create a new node, have last item of list point to
            # new item, point tail to the new item, and that adds it
            # into the new list.
            # if there isn't any items in the list we'll need to point
            # head and tail to the new item.
        '''
        new_node = Node(value) #creates the node
        if self.head is None:  #basically checks if list is empty to begin with
            self.head = new_node
            self.tail = new_node
        else: #if there is stuff in the list set next and tail to new node
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True


    def pop(self):
        if self.length == 0:  #takes care of case where the list is empty
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp




'''my_linked_list = LinkedList(4) 
#this creates the node, the head point, tail pointer, and pointer to next
print(my_linked_list.head.value)  #4
print(my_linked_list.length)

my_linked_list.append(2)
print(my_linked_list.tail.value)
print(my_linked_list.length)
my_linked_list.print_list()'''

my_linked_list = LinkedList(1)
my_linked_list.append(2)
print(my_linked_list.pop().value)
print(my_linked_list.pop())
print(my_linked_list.pop())

