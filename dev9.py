def pallindrome(num):
    original=num
    reversed_num=0
    while num>0:
        digit=num%10
        reversed_num=reversed_num*10+digit
        num=num//10
    return  original==reversed_num

def print_palindrome(start,end):
    for i in range(start,end+1):
        if pallindrome(i):
            print(i)

print_palindrome(1,1000)
    
