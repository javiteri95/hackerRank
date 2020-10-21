
def extraLongFactorials(n):
    if n == 0:
        return 1
    return n * extraLongFactorials(n-1)

if __name__ == "__main__":
    n = 6
    factorialN = extraLongFactorials(n)
    print(factorialN)