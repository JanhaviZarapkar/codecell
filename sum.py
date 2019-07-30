num1= 10
num2= 100
num3= 200

if num1 < 0:
   print("Enter a positive number")
else:
   sum1 = 0

   while(num1 > 0):
       sum1+= num1
       num1 -= 1
   print("The sum is",sum1)

if num2 < 0:
    print("Enter a positive number")
else:
    sum2 = 0

    while (num2 > 0):
        sum2 += num2
        num2 -= 1
    print("The sum is", sum2)

if num3 < 0:
    print("Enter a positive number")
else:
    sum3 = 0

    while (num3 > 0):
        sum3 += num3
        num3 -= 1
    print("The sum is", sum3)

print("Answer:",sum1+sum2+sum3)
