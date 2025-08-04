num=123
original=num
rev=0
while num>0:
    digit = num%10
    rev= rev*10+digit
    num=num//10
if(rev==original):
    print("number is pallindrome")
else:
    print("no is not pallindrome")
print("reverse of the number",rev)
