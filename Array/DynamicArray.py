# ===================== Create Dynamic Array =============================== o(1)


# capacity = 2
# arr = [None] * capacity
# size = 0

# print("Array =", arr)
# print("Size =", size)
# print("Capacity =", capacity)



# ===================== Append elements =============================== o(n)


# capacity = 2
# arr = [None] * capacity
# size = 0

# arr[size] = 6
# size += 1

# arr[size] = 10
# size += 1

# print("Array =", arr)
# print("Size =", size)
# print("Capacity =", capacity)



# ================= Append when FULL (RESIZE happens) ========================== o(n)


# capacity = 2
# arr = [10, 8]
# size = 2

# if size == capacity:
#     new_capacity = capacity * 2
#     new_arr = [None] * new_capacity

#     for i in range(size):
#         new_arr[i] = arr[i]

#     arr = new_arr
#     capacity = new_capacity

# arr[size] = 23
# size += 1

# print("Array =", new_arr)
# print("Size =", size)
# print("Capacity =", new_capacity)



# ================= Delete from Dynamic Array ========================== o(n)


capacity = 4
arr = [10, 23, 3, 5]
size = 4

delete_index = 2

for i in range(delete_index, size - 1):
    arr[i] = arr[i + 1]

arr[size - 1] = None
size -= 1

print("Array =", arr)
print("Capacity =", capacity)
print("Size =", size)