
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here
    beggining_pages = p // 2
    final_pages = (n + 1 - p) // 2 if n % 2 == 0 else (n - p) // 2

    return min([beggining_pages, final_pages])


if __name__ == '__main__':
    n = 6
    p = 5
    pages = pageCount(n, p)
    print(pages)