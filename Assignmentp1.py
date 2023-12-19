#write a program to find odd or even number using conditional statement

num = int (input ("Enter a number to check whether odd or even:"))
if (num % 2) == 0:
 print (num,"is an even Number")
else:
 print (num,"is an odd Number")


 #⁠find largest of three numbers

num1=int(input("enter 1st number"))
num2=int(input("enter 2nd number"))
num3=int(input("enter 3rd number"))
if (num1>=num2) and (num1 >= num3):
  print(num1,"is largest")
elif (num2 >= num1) and (num2 >= num3):
  print(num2,"is largest") 
else:
  print(num3,"is largest")

#find leap year using conditional statement
n=int(input("enter the year"))
if n%4==0:
    if n%400==0 or n%100!=0:
        print("the year is  a leap year")
    else:
        print("the year is not a leap year")
else:
    print("the year is not a leap year")

#⁠find summing numbers using while loop
n=int(input("enter the number"))
sum=0
i=1
while i<=n:
  sum+=i
  i+=1
print("sum of the number",sum)


#find countdown of a number using while loop
n=int(input("enter the number"))
while n>=0:
    print(n)
    n-=1


