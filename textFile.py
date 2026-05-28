file = open("demo.txt", "r")
print(file.read()) # Read and print file content
file.close()

file = open("demo1.txt","w")
file.write("helloooooo")
print(file.read())
file.close()