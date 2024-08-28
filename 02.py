s=input("enter  string")
up=0
lw=0
al=0
nm=0
sp=0


for i in s:
    if i.isupper():
       up=up+1
    elif i.islower():
        lw=lw+1
    if i.isalpha():
        al=al+1
    elif i.isnumeric():
        nm=nm+1
    if i.isspace():
        sp=sp+1

print("upper",up)
print("lower",lw)
print("alphabet",al)
print("numeric",nm)
print("space",sp)
