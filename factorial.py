def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        result = 1
        for i in range(2, num+1):
            result *= i
        return result

number = int(input("Enter the number: "))
fact = factorial(number)
print(f"The factorial of {number} is {fact}")