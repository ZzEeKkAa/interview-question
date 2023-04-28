# This is the small script that check if number is part of the fibonacci
# sequence.

FibArray = [1, 1]

def fibonacci(n):
    if n < 0:
        print("Incorrect input")

    elif n < len(FibArray):
        return FibArray[n]
    else:
        FibArray.append(fibonacci(n - 1) + fibonacci(n - 2))
        return FibArray[n]

num = int(input["Enter Fibonacci number to check :"])
for i in FibArray:
    if i = num:
        print(f"{num} is {i}'th number in fibonacci sequence")

print(f"{num} is not part of the fibonacci sequence")
