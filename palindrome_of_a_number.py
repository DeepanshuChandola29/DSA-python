num = int(input("Enter a number: "))
n = num
result = 0
while n>0:
    last_digit = n%10
    result = result*10 + last_digit
    n = n//10
if num == result:
    print (num , "is a palindrome")
else:
    print(num,"is not a palindrome")
