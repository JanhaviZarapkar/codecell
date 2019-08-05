
#import numpy as np
#n=5
#sum = 0
#l=[]
#l2=[]
#for i in range(1, n + 1):
  #  sum = i * i * i

 #   l2.append(sum)

#print(l2)
#result = [sum(int(digit) for digit in str(number)) for number in l]

#print(result)
#the_sum = sum(int(char) for j in l for char in str(j))
#print(the_sum)
#number = 0
#for element in l:
  #  my_string = str(element)
 #   for i in range(len(my_string)):
#        number += int(my_string[i])
#print(number)
def f(n):
    z=n%3
    m=n//3
    if(z==1):
        s=18*m+1
    elif(z==2):
        s=18*m+9
    return s
l=[5,500,5000000000]
a=[]
for i in l:
    a.append(f(i))
print(a)
m=1
for i in a:
    m=m*i
print(m%1000007)