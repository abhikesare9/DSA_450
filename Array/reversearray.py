def reverse(a):
    return a[::-1]

if __name__ == '__main__':
    a = [1,2,3,4]
    b = reverse(a)
    for i in range(len(b)):
        print(b[i])
