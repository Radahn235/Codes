n = int(input("Enter the number: "))
arm = 0
original=n
while n > 0:
    rem = n % 10
    arm += rem ** 3
    n = n // 10

if original == arm:
    print("The number is an Armstrong number")
else:
    print("The number is not an Armstrong number")
