
def staircase(number_of_steps):
    for i in range(1, number_of_steps + 1):
        print((number_of_steps - i) * " ", end="")
        print(i * "#")

n = 6
staircase(n)
