def movenegative(arr):
    high = len(arr)-1
    for i in range(int(len(arr)/2)):
        if arr[i] < 0:
            arr[i],arr[high] = arr[high],arr[i]
            high-=1




if __name__ == '__main__':
    arr = [1,-2,4,-9,11]
    movenegative(arr)
    for i in range(len(arr)):
        print(arr[i],end=' ')
    