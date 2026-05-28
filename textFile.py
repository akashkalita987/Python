# Step 1: Write to the file
with open("demo1.txt", "w") as file:
    file.write("helloooooo")

# Step 2: Open it again to read
with open("demo1.txt", "r") as file:
    print(file.read())