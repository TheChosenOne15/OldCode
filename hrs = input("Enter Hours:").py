hrs = input("Enter Hours:")
h = float(hrs)
perHour = input("Enter hourly rate:") 
pay = float(0)
if h <= 40 :
    pay = (float(perHour)) * h
elif h > 40 :
    pay = (float(perHour) * 1.5) * h
        
print (pay)