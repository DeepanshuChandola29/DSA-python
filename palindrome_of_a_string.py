string = input("Enter a string: ")
n = len(string)
left = 0
right = n - 1
while left < right:
    if string[left] != string[right]:
        print(string, "is not a palindrome.")
        break
    left += 1
    right -= 1
else:    
    print(string, "is a palindrome.")