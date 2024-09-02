no=int(input("give me a number: "))
a =[]
for i in range(1,no+1):
    if no%i==0:
        a.append(i)
print(a)