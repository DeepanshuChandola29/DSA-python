num = int(input("Enter a number: "))
n= num
total = 0
nod = len(str(num))
while n>0:
    last_digit = n%10
    total = total + last_digit**nod
    n = n//10
if num == total:
    print (num , "is an armstrong number")
else:
    print(num,"is not an armstrong number")