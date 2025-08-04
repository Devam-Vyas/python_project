def is_pallindrome(n):
    original=n
    reversed_num=0
    while n>0:
        digit=n%10
        reversed_num=reversed_num*10+digit
        n=n//10
    return original==reversed_num

for i in range(1001):
    if is_pallindrome(i):
        print(i)
