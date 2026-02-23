#Website server overloading alert
user = int(input("Enter number of users currently online: "))

if user< 50:
    print("Traffic is LOW. Server is running smoothly.")
elif user < 200:
    print("Traffic is MEDIUM. Monitor server performance.")
else:
    print("Traffic is HIGH! Trigger alert and scale server resources.")
