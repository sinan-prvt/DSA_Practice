# ===================== Create an Array =============================== o(1)


# capacity = 5
# arr = [None] * capacity
# size = 0

# print("Array", arr)
# print("Capacity", capacity)
# print("size", size)



# ===================== Add elements (Append) =============================== o(1)


# capacity = 5
# arr = [None] * capacity
# size = 0

# arr[size] = 10
# size += 1

# arr[size] = 5
# size += 1

# print("Array =", arr)
# print("Size =", size)



# ===================== Read an element =============================== o(1)


# arr = [10, 30, None, None, None]

# print("Element at index 0:", arr[0])
# print("Element at index 1:", arr[1])
# print("Element at index 4:", arr[4])



# ===================== Insert in the middle =============================== o(n)


# capacity = 5
# arr = [None] * capacity
# size = 0

# arr[size] = 10
# size += 1

# arr[size] = 6
# size += 1

# for i in range(size, 1, -1):
#     arr[i] = arr[i - 1]

# arr[1] = 9
# size += 1

# print(arr)



# ===================== Delete an element =============================== o(n)


arr = [10, 8, 4, None, None]
size = 3

for i in range(1, size - 1):
    arr[i] = arr[i + 1]

arr[size - 1] = None
size -= 1

print("Array =", arr)
print("Size =", size)