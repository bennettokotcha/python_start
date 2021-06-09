def bubble_sort(lis):
    print(lis)
    for t in range(len(lis)-1):
        for i in range(len(lis)-1-t):
            if lis[i] > lis[i+1]:
                lis[i], lis[i+1] = lis[i+1], lis[i]
    return lis
print(bubble_sort([6,5,3,1,8,7,2,4]))