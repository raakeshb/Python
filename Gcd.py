x=int(input("Greatest one"))
y=int(input("Lowest one"))
m=1
while(m!=0):    #x=number * y, reminder
    div=int(x/y)
    mul=div*y
    dif=x-mul
    print(x,"=",div,"x",y,",",dif,"\n")
    x=y
    y=dif
    m=dif
