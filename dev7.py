
def armstrong(num):
    order=len(str(num))
    sum=0
    temp = num
    while temp>0:
        digit=temp%10
        sum=sum+digit**order
        temp=temp//10
    return sum==num
def print_armstrong_number(start,end):
    for i in range(start,end+1):
        if(armstrong(i)):
            print(i)

print_armstrong_number(1,1000)

    
