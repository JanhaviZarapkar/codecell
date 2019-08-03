#import datetime
#week_days= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
#l=list(map(int, input("Enter date \n eg: 11/12/1999 \n\n").split('/')))
#day=datetime.date(l[2],l[1],l[0]).weekday()
#print([day])
#print(week_days[day])
d=["02/01/1",
"28/02/100",
"16/05/1000",
"03/08/2019",
"31/02/2999",
"17/05/3400",
"31/01/9999999",
"31/12/999999999999"]
def day(d):
    A=[]
    l=d.split("/")
    for j in l:
        j=j.lstrip("0")
        A.append(j)

    mod=31*(int(A[1])-1)+int(A[0])+365*(int(A[2])-1)-1
    return(mod%7)

sum=0
for i in d:
    sum=sum+day(i)
print(sum)
