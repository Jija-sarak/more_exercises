list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16]
list3 =[]
i = 0
while i < len(list2):
    if list2[i] not in list3 :
        list3.append(list2[i])
    j = 0
    while j<len(list1):
        if list1[j] not in list3:
            list3.append(list1[j])
        j+=1
    i+=1
print(list3)
