# graph = {'A': ['B', 'D', 'E', 'F'], 'D': ['A'], 'B': ['A', 'F', 'C'], 'F': ['B', 'A'], 'C': ['B'], 'E': ['A']}
# print("Given Graph is:")
# print(graph)
#
#
# def dfs_traversal(input_graph, source):
#     stack = list()
#     visited_list = list()
#     stack.append(source)
#     visited_list.append(source)
#     while stack:
#         vertex = stack.pop()
#         print(vertex, end=" ")
#         for u in input_graph[vertex]:
#             if u not in visited_list:
#                 stack.append(u)
#                 visited_list.append(u)
#
#
# print("DFS traversal of graph with source A is:")
# dfs_traversal(graph, "A")

def freqAlphabets(s):
    """
    :type s: str
    :rtype: str
    """
    s_list = list(s)
    ptr1 = 0
    ptr2 = s.find("#")
    indx = ""
    ptr_list = []
    while True:
        indx += s_list[ptr2-2] + s_list[ptr2-1]
        for i in range(ptr1, ptr2-2):
            ptr_list.append(int(s_list[i]))
        ptr_list.append(int(indx))
        indx = ""

        ptr1 = ptr2 + 1
        ptr2 = s.find("#", ptr1)

        if ptr2 == -1:
            if ptr1 <= len(s_list)-1:
                for num in range(ptr1, len(s_list)):
                    ptr_list.append(int(s_list[num]))
                break
            else:
                break
    decrypt = ""

    for num in ptr_list:
        decrypt += chr(96+num)

    return decrypt

s = "26#11#418#5"
print(freqAlphabets(s))