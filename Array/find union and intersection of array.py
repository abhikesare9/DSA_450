def union(arr1,arr2):
    union = []
    for i in range(len(arr1)):
        union.append(arr1[i])
    for j in range(len(arr2)):
        union.append(arr2[i])

    union = set(union)
    return union


def intersection(arr1,arr2):
    intersec = []
    for j in range(len(arr2)):
        if arr2[j] in arr1:
            intersec.append(arr2[j])
    return intersec



if __name__ == '__main__':
    arr1 = [1,2,3,4,5]
    arr2 = [5,6,7,8,9]
    op = union(arr1,arr2)
    op1 = intersection(arr1,arr2)
    for item in op:
        print(item,end=' ')
    print('\n')
    for item in op1:
        print(item,end=' ')