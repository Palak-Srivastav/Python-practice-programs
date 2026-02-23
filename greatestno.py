# Print the number given that is greater than the required number from the list

#number = [10,50,90,66,102,76,80,43]
#count=0

#for n in number:
 #   if(n>40):
  #      count+= 1

#print("count", count)

#Different program to find greatest number in list
numbers = int(input("Enter list"))

max_num = numbers[0]

for n in numbers:
    if n > max_num:
        max_num = n

print("Maximum number is:", max_num)

