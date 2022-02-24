list1 = [1, 342, 75, 23, 98]
list2 = [75, 23, 98, 12, 78, 10, 1]
list3 = []
i = 0
while i < len(list1):
    if list1[i] in list2:
        list3.append(list1[i])
    i+=1
print(list3)
