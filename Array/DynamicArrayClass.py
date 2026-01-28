# ======================== Resize and append an Array ===============================


# class DynamicArray:
#     def __init__(self):
#         self.capacity = 2
#         self.size = 0
#         self.arr = [None] * self.capacity
    
#     def display(self):
#         print("Array =", self.arr)
#         print("Capacity =", self.capacity)
#         print("Size =", self.size)

#     def resize(self, new_capacity):
#         new_arr = [None] * new_capacity

#         for i in range(self.size):
#             new_arr[i] = self.arr[i]

#         self.arr = new_arr
#         self.capacity = new_capacity
    
#     def append(self, value):
#         if self.size == self.capacity:
#             self.resize(self.capacity * 2)
        
#         self.arr[self.size] = value
#         self.size += 1

# arr = DynamicArray()

# arr.append(10)
# arr.append(6)
# arr.append(3)

# arr.display()



# ======================== get an Array =============================== 



class DynamicArray:
    def __init__(self):
        self.capacity = 2
        self.size = 0
        self.arr = [None] * self.capacity

    def display(self):
        print("Array =", self.arr)
        print("Size =", self.size)
        print("Capacity =", self.capacity)
        print("-" * 30)

    def _resize(self, new_capacity):
        new_arr = [None] * new_capacity

        for i in range(self.size):
            new_arr[i] = self.arr[i]

        self.arr = new_arr
        self.capacity = new_capacity

    def append(self, value):
        if self.size == self.capacity:
            self._resize(self.capacity * 2)

        self.arr[self.size] = value
        self.size += 1

    def get(self, index):
        if index < 0 or index >= self.size:
            print("Index out of bounds")
            return None
        return self.arr[index]

arr = DynamicArray()

arr.append(10)
arr.append(20)
arr.display()

print("Element at index 1:", arr.get(1))


# ======================== Insert an Array =============================== 



# class DynamicArray:
#     def __init__(self):
#         self.capacity = 2
#         self.size = 0
#         self.arr = [None] * self.capacity

#     def display(self):
#         print("Array =", self.arr)
#         print("Capacity =", self.capacity)
#         print("Size =", self.size)

#     def resize(self, new_capacity):
#         new_arr = [None] * new_capacity

#         for i in range(self.size):
#             new_arr[i] = self.arr[i]
        
#         self.arr = new_arr
#         self.capacity = new_capacity
    
#     def append(self, value):
#         if self.size == self.capacity:
#             self.resize(self.capacity * 2)
        
#         self.arr[self.size] = value
#         self.size += 1

#     def insert(self, index, value):
#         if index < 0 or index > self.size:
#             print("Invalid index")
#             return 
        
#         if self.size == self.capacity:
#             self.resize(self.capacity * 2)

#         for i in range(self.size, index, -1):
#             self.arr[i] = self.arr[i - 1]
        
#         self.arr[index] = value
#         self.size += 1
    
# arr = DynamicArray()

# arr.append(10)
# arr.append(5)
# arr.append(76)
# arr.append(6)

# arr.insert(1, 3)
# arr.display()



# ======================== Delete an Array =============================== 


# class DynamicArray:
#     def __init__(self):
#         self.capacity = 2
#         self.size = 0
#         self.arr = [None] * self.capacity
    
#     def display(self):
#         print("Array =", self.arr)
#         print("Capacity =", self.capacity)
#         print("Size =", self.size)
    
#     def resize(self, new_capacity):
#         new_arr = [None] * new_capacity

#         for i in range(self.size):
#             new_arr[i] = self.arr[i]
        
#         self.arr = new_arr
#         self.capacity = new_capacity
    
#     def append(self, value):
#         if self.size == self.capacity:
#             self.resize(self.capacity * 2)
        
#         self.arr[self.size] = value
#         self.size += 1
    
#     def delete(self, index):
#         if index < 0 or index > self.size:
#             print("Invalid index")
#             return
        
#         for i in range(index, self.size - 1):
#             self.arr[i] = self.arr[i + 1]
        
#         self.arr[self.size - 1] = None
#         self.size -= 1


# arr = DynamicArray()

# arr.append(10)
# arr.append(3)
# arr.append(8)

# arr.delete(1)
# arr.display()