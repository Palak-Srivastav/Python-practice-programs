def marksheet(name, marks):
    avg = sum(marks) / len(marks)
    if avg >= 75: result = "Distinction"
    elif avg >= 35: result = "Pass"
    else: result = "Fail"
    print(name, "Average:", avg, "| Result:", result)

marksheet("Palak", [80, 70, 60])
