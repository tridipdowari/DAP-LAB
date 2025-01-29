def countCaseLetters(s):
    upperCaseCount = 0
    lowerCaseCount = 0

    for char in s:
        if char.isupper():
            upperCaseCount += 1
        elif char.islower():
            lowerCaseCount += 1
    return upperCaseCount, lowerCaseCount

string = input("Enter the string: ")
upper, lower = countCaseLetters(string)

print(f"Uppercase letters: {upper}")
print(f"Lowercase letters: {lower}")