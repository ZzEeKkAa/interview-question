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
    '''
        assume Key is <-- Looking for
    '''
    if n < 0:
        print("Incorrect input")

    elif n < len(FibArray):
        return n 
    else:
        FibArray.append(fibonacci(n - 1) + fibonacci(n - 2))
        return n

UserIp = int(input("Enter Fibonacci number to check :"))
fibonacci(100)
for number in FibArray:
    if number == UserIp:
        if (UserIp == 1):
            print(f"{UserIp} is {1}'st or 2nd number in fibonacci sequence")
            exit()
        else:
            print(f"{UserIp} is {FibArray.index(number)}'th number in fibonacci sequence")
            exit()

print(f"{UserIp} is not part of the fibonacci sequence")
