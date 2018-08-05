# Write your solution for 1.1 here!
x = 0
for i in range(1000):
    if i%6==2:
        if i**3%5==3:
            x=i
print(x)