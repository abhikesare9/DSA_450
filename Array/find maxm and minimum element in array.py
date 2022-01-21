
def findmaxandmin(a):
    max_ele = -1
    min_ele = 99999
    for i in range(len(a)):
        if a[i] > max_ele:
            max_ele = a[i]
        if a[i] < min_ele:
            min_ele = a[i]

    return (min_ele,max_ele)

if __name__ == '__main__':
    a = [1,2,3,4,5,6]
    op = findmaxandmin(a)
    print(op)
    
   

