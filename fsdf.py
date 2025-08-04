no1=int(input("Enter no1"))
no2=int(input("Enter no2"))
no3=int(input("Enter no3"))
no4=int(input("Enter no4"))
no5=int(input("Enter no5"))
fail_subject=False
if(no1<36):
    print("back in first subject")
    fail_subject=True
if(no2<36):
    print("back in second subject")
    fail_subject=True
if(no3<36):
    print("back in third subject")
    fail_subject=True
if(no4<36):
    print("back in fourth subject")
    fail_subject=True
if(no5<36):
    print("back in fifth subject")
    fail_subject=True
    
sum=no1+no2+no3+no4+no5
per= sum/500*100
if(fail_subject==False):
    if(per<36):
        print("you got failed in the subject",per)
    elif(per>36and per<45):
        print("you got passed with third divsion",per)
    elif(per>45and per<60):
        print("you got passed with second division",per)
    if(per>60):
        print("you got passed with second division",per)    
    
