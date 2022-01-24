def leftrotatebyone(arr):
  temp = arr[0]
  for i in range(len(arr)-1):
      arr[i] = arr[i+1]

  arr[len(arr)-1] = temp

if __name__ == '__main__':
    arr = [1,2,3,4,5]
    leftrotatebyone(arr)
    for i in range(len(arr)):
        print(arr[i],end=" ")