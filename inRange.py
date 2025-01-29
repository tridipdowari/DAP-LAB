def isInRange(num, start, end):
    return start <= num <= end

num = int(input("Enter the number: "))
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

if isInRange(num, start, end):
    print(f"{num} is in the range between {start} and {end}")
else:
    print(f"{num} is not in the range between {start} and {end}")