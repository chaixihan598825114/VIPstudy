# list1 = [1,2,3,4,5,6,7,8,9]
# res = 17
# # for i in list1:
# #     for j in list1:
# #         if i + j == res:
# #             print(i,j)
#
# for n in list1:
#     for m in list1:
#         if n + m == res:
#             print(n,m)

file = open('data.txt','r')

file_mation = file.readlines()

file.close()

dict1 = {}
list1 = []
for i in file_mation:
    i = i.strip()
    list1 = i.split('，')
    # print(list1)
    for j in list1:
        list2 = j.split(':')
        # print(list2)
        dict1[list2[0]] = int(list2[1])
# print(dict1)

for k,v in dict1.items():
    if v > 18:
        print(k,end=' ')



