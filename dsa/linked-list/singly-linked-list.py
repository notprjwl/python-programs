# creating node class 
class node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        
# linked list class
class linked_list:
    def __init__(self): 
        self.head = node()
    
    # appending new node    
    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    # returning the length   
    def length(self):
        total = 0
        cur = self.head
        while cur.next != None:
            total += 1
            cur = cur.next
        return total
    
    # displaying the list
    def display(self):
        elem = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elem.append(cur_node.data)
        print (elem)
    
    # getting the element using the position
    def get_elem(self, index):
        if index >= self.length():
            print("ERR: Index out of range!")
            return None
        cur_index = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_index == index: 
                return cur_node.data
            cur_index += 1
    
    # getting the index from element
    def get_index(self, elem):
        cur_node = self.head
        index = 0
        while cur_node.next != None:
            cur_node = cur_node.next
            if cur_node.data == elem:
                return index
            index += 1
        print("ERR element not found in the list!")
        return None
    
    # deleting element
    def delete_elem(self, index):
        if index >= self.length():
            print('ERR: Index out of range!')    
            return None
        cur_index = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_index == index:
                last_node.next = cur_node.next
                return 
            cur_index += 1  
 
my_list = linked_list()

my_list.display()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)

print(f"element at the 2nd position is {my_list.get_elem(2)}")
print(f"index of the element 4 is {my_list.get_index(4)}")

my_list.display()

print(f"element deleted at the index 3 {my_list.delete_elem(3)}")

my_list.display()


