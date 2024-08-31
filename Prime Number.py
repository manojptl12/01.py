n=int(input("enter N:"))
if n%2!=0:
    for i in range(3,int(n/2)+1,2):
        if n%i==0:
           print(n,"Is not a prime")
           break

    else:
         print(n,"Is a prime")

else:
    print(n,"Is not a prime")
