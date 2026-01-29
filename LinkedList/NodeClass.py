# ============================== Insert at Beginning ========================================



# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
    
# class LinkedList:
#     def __init__(self):
#         self.head = None
    
#     def insert_fst(self, data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node
    
#     def display(self):
#         temp = self.head
#         while temp is not None:
#             print(temp.data, end="->")
#             temp = temp.next

# l = LinkedList()

# l.insert_fst(1)
# l.insert_fst(2)
# l.insert_fst(3)
# l.insert_fst(4)

# l.display()




# ============================== Insert at End ========================================



# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
    
# class LinkedList:
#     def __init__(self):
#         self.head = None
    
#     def intert_fst(self, data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node
    
#     def insert_end(self, data):
#         new_node = Node(data)

#         if self.head is None:
#             self.head = new_node
#             return
    
#         temp = self.head
#         while temp.next is not None:
#             temp = temp.next
        
#         temp.next = new_node

#     def display(self):
#         temp = self.head
#         while temp is not None:
#             print(temp.data, end="->")
#             temp = temp.next
#         print("None")


# l = LinkedList()

# l.insert_end(1)
# l.insert_end(2)
# l.insert_end(3)

# l.display()
