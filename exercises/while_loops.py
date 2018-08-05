# Write your solution for 1.3 here!
sum = 0
x = 0
c = 0
while sum<10000:
    if (x%2==0):
        sum+=x
        x+=1
        c+=1
    else:
        x+=1
print("numbers of numbers:", c)
print("the biggest number is:", x)
print("sum:", sum)