# This is the small script that check if number is part of the fibonacci
# sequence.

FibArray = [1, 1]
'''
Function:
    Function generates fibonacci sequence

Input/Output:
    Input: sequence length
    Output: nothing/ FibArray
'''
def fibonacci(n):
    if n < 0:
        print("Incorrect input")

    elif n < len(FibArray):
        return FibArray[n]
    else:
        FibArray.append(fibonacci(n - 1) + fibonacci(n - 2))
        return FibArray[n]

UserIp = int(input("Enter Fibonacci number to check :"))
fibonacci(num)
for index in FibArray:
    if index == UserIp:
        if (UserIp == 1):
            print(f"{num} is {1}'st number in fibonacci sequence")
            print(f"{num} is {2}'nd number in fibonacci sequence")
            exit()
        else:
            print(f"{num} is {i}'th number in fibonacci sequence")
            exit()

print(f"{num} is not part of the fibonacci sequence")
