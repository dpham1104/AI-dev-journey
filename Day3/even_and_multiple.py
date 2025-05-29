num = int(input("Enter a number: "))

if num % 2 == 0 and num % 3 == 0:
    print("It is even and a multiple of 3")
elif num%2==0 and num%3 != 0:
    print("It is even but not a multiple of 3")
elif num%2!=0 and num%3==0:
    print("It is a multiple of 3 but not even")
else:
    print("It is not even and a multiple of 3")