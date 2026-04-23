n = int(input("Enter a number: "))
result=[]
for i in range (1 , n+1):
    if n%i == 0:
        result.append(i)
print("Factors of ",n , "are:" , result)
