a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a > b:
    x=a
    a=b
    b=x
if a > c:
    y=a
    a=c
    c=y
if b > c:
    z=b
    b=c
    c=z
print(a," ", b," ", c)