def next_greater(nums1, nums2):
    output = []
    for i in range(len(nums1)):
        found = False
        for j in range(len(nums2)):
            if nums2[j] == nums1[i]:
                for k in range(j, len(nums2)):
                    if nums2[k] > nums1[i]:
                        output.append(nums2[k])
                        found = True
                        break
                if not found:
                    output.append(-1)

    return output

nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(next_greater(nums1, nums2))

