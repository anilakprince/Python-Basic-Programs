#Write a program to create a list of fruits and copy only 'e' letter fruits to the new list

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
 for x in fruits:
  if "e" in x:
    newlist.append(x)
  return newlist
print(copy())


#write Pgm to find prime number or not

num = int(input("Enter any number: "))

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           break
   else:
       print(num,"is a prime number")
       

else: #if num <= 1, it is not prime
   print(num,"is not a prime number")

