#program to alert user on low battery

battery = int(input("Enter current battery:"))

if battery>50:
   print("Battery will last long")
elif battery>20:
   print("Advised to charge phone now")
else:
   print("Phone will be dead,CHARGE NOW")

    
              