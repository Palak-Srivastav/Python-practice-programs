try:
    f = open("ffile.txt", "r")
    content = f.read()
    print(content)
    f.close()

except FileNotFoundError:
    print("Error: File not found.")

except Exception as e:
    print("Unexpected error:", e)
