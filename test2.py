def fibonacci(n):

    # This print out numbers
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

if __name__ == "__main__":
    fibonacci(10)
