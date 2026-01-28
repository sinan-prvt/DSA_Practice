# ===================== Create an Array =============================== o(1)


# class StaticArray:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.size = 0
#         self.arr = [None] * self.capacity

#     def display(self):
#         print("Array =", self.arr)
#         print("Capacity =", self.capacity)
#         print("Size =", self.size)

# arr = StaticArray(5)

# arr.display()



# ===================== Append Element =============================== o(1)


# class StaticArray:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.size = 0
#         self.arr = [None] * capacity

#     def display(self):
#         print("Array =", self.arr)
#         print("Capacity =", self.capacity)
#         print("Size =", self.size)

#     def append(self, value):
#         if self.size == self.capacity:
#             print("Array is Full")
#             return

#         self.arr[self.size] = value
#         self.size += 1

# arr = StaticArray(5)

# arr.append(10)
# arr.append(5)
# arr.append(9)
# arr.append(45)
# arr.display()


# ===================== Get Element =============================== o(1)


# class StaticArray:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.size = 0
#         self.arr = [None] * capacity

#     def display(self):
#         print("Array =", self.arr)
#         print("Capacity =", self.capacity)
#         print("Size =", self.size)

#     def append(self, value):
#         if self.size == self.capacity:
#             print("Array is Full")
#             return

#         self.arr[self.size] = value
#         self.size += 1

#     def get(self, index):
#         if index < 0 or index > self.size:
#             print("Invalid Index")
#             return None
#         return self.arr[index]


# arr = StaticArray(5)

# arr.append(10)
# arr.append(5)
# arr.append(9)
# arr.append(45)

# print("Element at index 1 =", arr.get(1))



# ===================== Insert Element =============================== o(n)


# class StaticArray:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.size = 0
#         self.arr = [None] * capacity

#     def display(self):
#         print("Array =", self.arr)
#         print("Capacity =", self.capacity)
#         print("Size =", self.size)

#     def append(self, value):
#         if self.size == self.capacity:
#             print("Array is Full")
#             return

#         self.arr[self.size] = value
#         self.size += 1

#     def insert(self, index, value):
#         if self.size == self.capacity:
#             print("Array is Full")
#             return
        
#         if index < 0 or index > self.size:
#             print("Invalid Index")
#             return

#         for i in range(self.size, index, -1):
#             self.arr[i] = self.arr[i - 1]    

#         self.arr[index] = value
#         self.size += 1

# arr = StaticArray(5)

# arr.append(10)
# arr.append(5)
# arr.append(9)

# arr.insert(1, 40)
# arr.display()



# ===================== Delete Element =============================== o(n)


class StaticArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.arr = [None] * capacity

    def display(self):
        print("Array =", self.arr)
        print("Capacity =", self.capacity)
        print("Size =", self.size)

    def append(self, value):
        if self.size == self.capacity:
            print("Array is Full")
            return
        
        self.arr[self.size] = value
        self.size += 1
    
    def delete(self, index):
        if index < 0 or index > self.size:
            print("Invalid Index")
            return
    
        for i in range(index, self.size - 1):
            self.arr[i] = self.arr[i + 1]

        self.arr[self.size - 1] = None
        self.size += 1

arr = StaticArray(5)

arr.append(10)
arr.append(3)
arr.append(7)

arr.delete(1)
arr.display()