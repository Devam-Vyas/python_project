salary=int(input("Enter salary"))
if(salary>35000):
    ta=salary*0.05
    da=salary*0.05
    hra=2000
    salary=salary+ta+da+hra
    print(salary)
elif(salary>25000):
    ta=35000*0.05
    da=35000*0.05
    hra=1000
    salary=salary+ta+da+hra
    print(salary)
elif(salary>15000):
    ta=35000*0.05
    da=35000*0.05
    hra=1000
    salary=salary+ta+da+hra
    print(salary)
else:
    print(salary)
    
    
