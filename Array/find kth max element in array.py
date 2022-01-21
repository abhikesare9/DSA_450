

#quick sort
from unittest import result


def partition(arr,low,high):
    i = low -1
    pivot = arr[high]  #picking last element as pivot
    for j in range(low,high):
        if arr[j] <= pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return (i+1)

def quicksort(arr,low,high):
    if len(arr) == 1:
        return
    if low<high:
        pi = partition(arr,low,high)
        quicksort(arr,low+1,pi-1)
        quicksort(arr,pi+1,high)

def findkthmaximum(arr,k):
    n = len(arr)
    result = arr[n-k-1]
    return result
def findkthminimum(arr,k):
    n = len(arr)
    result = arr[k]
    return result

if __name__=='__main__':
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    quicksort(arr, 0, n-1)
    max = findkthmaximum(arr,3)
    min = findkthminimum(arr,5)
    print(max,min)