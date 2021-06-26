def compareTriplets(a, b):
    # Write your code here
    aliceMayors = [x for (i,x) in enumerate(a) for (j,y) in enumerate(b) if x > y and i == j]
    bobMayors = [x for (i,x) in enumerate(a) for (j,y) in enumerate(b) if x < y and i == j]

    return [len(aliceMayors), len(bobMayors)]

if __name__ == '__main__':
    a = [2,5,8,12,6,8,7]
    b = [4,5,7,9,7,10,7]

    result = compareTriplets(a,b)
    print(result)
