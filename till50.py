# Generating code to print all prime number between 0 to 50

for i in range(0, 51):
    is_prime = True

for num in range(2,num):
    if num%i==2:
        is_prime = False
        break

if is_prime:
    print(num)
