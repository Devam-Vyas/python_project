def isArmstrong(n):
    num=n
    power=len(str(n))
    total=0
    while n>0:
        digit=n%10
        total=total+digit**power
        n=n//10
    return total==num
for i in range(1001):
    if(isArmstrong(i)):
        print(i)
        
