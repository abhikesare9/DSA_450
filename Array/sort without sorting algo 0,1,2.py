def sort012(arr):
    low = 0
    mid = 0
    high = len(arr)-1

    while mid <= high:
        if arr[mid] == 0:
            arr[low],arr[mid] = arr[mid],arr[low]
            mid+=1
            low +=1
        elif arr[mid] ==1:
            mid += 1
        else:
            arr[mid],arr[high] = arr[high],arr[mid]
            high -=1




if __name__ == '__main__':
    arr = [1,0,0]
    sort012(arr)
    for i in range(len(arr)):
        print(arr[i],end=' ')