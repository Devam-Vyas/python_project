unit=int(input("Enter unit"))
if(unit<100 and unit>0):
    billamount=unit*3
    print(billamount)
if(unit<200 and unit>100):
    billamount=300+(unit-100)*5
    print(billamount)
elif(unit<200 and unit>100):
    billamount=300+(unit-100)*5
    print(billamount)
elif(unit<300 and unit>200):
    billamount=300+500+(unit-200)*7
    print(billamount)
else:
    billamount=300+500+700+(unit-300)*10
    print(billamount)
