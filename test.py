l =[4,3,2,1]
i = 0
indiceminimum = 0
while(i<len(l)):
    if(l[i]<l[indiceminimum]):
        indiceminimum=i
    i=i+1
    
print(indiceminimum)