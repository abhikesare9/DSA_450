from asyncio import current_task
import sys

def maxsum(arr):
    n = len(arr)
    max_sum =  -(sys.maxsize) - 1
    curr_sum = 0

    for i in range(0,n):
        curr_sum += arr[i]
        if curr_sum > max_sum:
            max_sum = curr_sum
        if curr_sum < 0:
            curr_sum = 0
    return max_sum





if __name__ == '__main__':
    arr = [1,2,3,-2,5]
    op = maxsum(arr)
    print(op)
