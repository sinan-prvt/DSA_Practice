# ======================= Reverse an array =============================


# arr = [1,2,3,4,5]

# left = 0
# right = len(arr) - 1

# while left < right:
#     arr[left], arr[right] = arr[right], arr[left]
#     left += 1
#     right -= 1

# print(arr)




# ======================= Check if array is palindrome =============================


# arr = [1,2,3,2,1]

# left = 0
# right = len(arr) - 1
# is_palindrome = True

# while left < right:
#     if arr[left] != arr[right]:
#         is_palindrome = False
#         break

#     left += 1
#     right -= 1

# print(is_palindrome)




# ======================= Find pair with given sum =============================


# arr = [1, 2, 3, 4, 6]
# target = 10

# left = 0
# right = len(arr) - 1

# found = False

# while left < right:
#     current_sum = arr[left] + arr[right]

#     if current_sum == target:
#         print("Pair Found =", arr[left], arr[right])
#         found = True
#         break
#     elif current_sum < target:
#         left += 1
#     else:
#         right -= 1
    
# if not found:
#     print("Not Found")




# ======================= Move all zeros to the end =============================


arr = [0, 1, 0, 3, 12]

left = 0

for right in range(len(arr)):
    if arr[right] != 0:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
    
print(arr)

