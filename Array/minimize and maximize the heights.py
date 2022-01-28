def getminimumdiff(arr,k):
    arr.sort()
    n = len(arr)
    ans = arr[n-1] - arr[0]
    smallest = arr[0]+k
    largest = arr[n-1]-k

    for  i in range(n):
        mi = min(smallest,arr[i]-k)
        ma = max(largest,arr[i]+k)
        if mi<0:
            continue
        ans = min(ans,ma-mi)

    return ans

if __name__ == '__main__':
    A = [3,9,12,16,20]
    op = getminimumdiff(A,3)
    print(op)


"""
step 1: sort the array 
step 2: get smallest element by add k to it 
step 3: get largest element by subtracting k from it 
step 4: get answer by subtracting smallest from largest
step 5: run a loop from array calculate minimum and maximum element ans as difference if difference is minimum that previous return it
"""