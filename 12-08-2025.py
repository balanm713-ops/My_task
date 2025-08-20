# 3.prime or not  
a=int(input())
if a<=1:
    print("not prime")
else:
    b=True
    c=0
    for i in range(1,a+1):
        if i*i>a:
            c=i-1
            break
    for i in range(2,c+1):
        if a%i==0:
            b=False
            break
    if b:
        print("prime")
    else:
        print("not prime")