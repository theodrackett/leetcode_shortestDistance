def findDisappearedNumbers(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    output = []
    ashy = {}

    for num in nums:
        ashy[num] = 1

    for num in range(1, len(nums) + 1):
        if num not in ashy:
            output.append(num)

    return output


mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]
j = 0
for i in range(len(mat)):
    for j in range(i+j+1):
        print(mat[i][j])


# print(mat[0][1])
# print(mat[1][0])
# print(mat[2][0])
# print(mat[1][1])
# print(mat[0][2])
# print(mat[1][2])
# print(mat[2][1])
# print(mat[2][2])

# for i in range(len(mat)):
#     for j in range(len(mat[i])):
#         print(mat[i][j])


# nums = [1, 2, 3, 4, 7, 8]
# nums = [1, 1]
nums = [4, 3, 2, 7, 8, 2, 3]
#print(findDisappearedNumbers(nums))

# def thirdMax(nums):
#     """
#     :type num_array: List[int]
#     :rtype: int
#     """
#     num_array = sorted(nums)
#     #num_array = list(dict.fromkeys(num_array))
#     no_dup = []
#
#     for num in num_array:
#         if num not in no_dup:
#             no_dup.append(num)
#     print(no_dup)
#     if len(no_dup) == 1:
#         return no_dup[0]
#     if len(no_dup) == 2:
#         return no_dup[1]
#
#     first = no_dup[2]
#     second = no_dup[1]
#     third = no_dup[0]
#
#     for i in range(3, len(no_dup)):
#         if no_dup[i] > first:
#             third = second
#             second = first
#             first = no_dup[i]
#
#     return third
#
# nums = [1,2, 2, 3]
# print(thirdMax(nums))
