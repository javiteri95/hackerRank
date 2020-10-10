import functools 

def aVeryBigSum(ar):
    return functools.reduce(lambda a,b : a+b , ar)

if __name__ == "__main__":
    ar = [1,2,3,4]
    sum = aVeryBigSum(ar)
    print(sum)