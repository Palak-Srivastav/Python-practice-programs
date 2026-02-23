import json

# Open the file and load the data
with open('data.json', 'r') as f:
    data = json.load(f)

# Print the data to show it works
print("Name:", data['name'])
print("Shop Item 1:", data['shopItem'][0])
print("Nested Marks:", data['myObj']['marks'])