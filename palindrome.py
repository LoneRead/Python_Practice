name=input("Enter a string: ")
string=name.lower()
original=[]
reverse=[]
for i in range(0, len(string)):
 original.append(string[i])
for i in range(1, len(string)+1):
 reverse.append(string[-i])
if original==reverse:
 print("Palindrome")
else:
 print("Not Palindrome")

