import enum
import random

target = 0
nums = [-3, 4, 3, 90]


# Fast Hashmap version

cool_map = {}
for i, x in enumerate(nums):
    remaining = target - x

    if remaining in cool_map:
        print(i, cool_map[remaining])

    cool_map[x] = i


# SLOW VERSION
# pointer_left = 0
# pointer_right = 1
# num_size = len(nums)

# for _ in range(num_size - 1):
#     # print(f"------{nums[pointer_left]}--------- index: {pointer_left}")

#     for y in range(num_size - pointer_right):
#         if nums[pointer_left] + nums[pointer_right] == target:
#             # print(nums[pointer_left] + nums[pointer_right])
#             print([pointer_left, pointer_right])
#         # print(f"{y} ----- {pointer_right}")

#         pointer_right += 1
#     pointer_left += 1
#     pointer_right = pointer_left + 1


# Random Version (No good)
# import random
# import math

# halfway = math.floor(len(nums) / 2)

# slice1, slice2 = nums[:halfway], nums[halfway:]

# x = slice1[0]
# y = slice2[0]

# len_slice1 = len(slice1)
# len_slice2 = len(slice2)

# index1, index2 = 0, halfway


# while x + y != target:
#     select = random.choice(range(3))

#     if select == 0:
#         # try two random numbers from the right slice
#         index1 = random.choice(range(len_slice1))
#         index2 = random.choice(range(len_slice1))
#         if index1 != index2:
#             x = slice1[index1]
#             y = slice1[index2]
#         else:
#             pass
#     elif select == 1:
#         # try 1 random number from the right slice, and one random number from the left slice
#         index1 = random.choice(range(len_slice1))
#         index2 = random.choice(range(len_slice2))
#         x = slice1[index1]
#         y = slice2[index2]
#         index2 += halfway
#     elif select == 2:
#         # try two random numbers from the right slice
#         index1 = random.choice(range(len_slice2))
#         index2 = random.choice(range(len_slice2))
#         if index1 != index2:
#             x = slice2[index1]
#             y = slice2[index2]
#             index1 += halfway
#             index2 += halfway
#         else:
#             pass

# print([index1, index2])
