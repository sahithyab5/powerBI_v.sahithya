# # Read the file
# with open("the-zen-of-python.txt", "r") as file:
#     print("Before appending:")
#     print(file.read())

# # Append a line
# with open("the-zen-of-python.txt", "a") as file:
#     file.write("\nAppended line: Hello from Python!")

# # Read again to see the result
# with open("the-zen-of-python.txt", "r") as file:
#     print("\nAfter appending:")
#     print(file.read())



file = open("the-zen-of-python.txt", "w")
file.write("Hello, World!")
file.close()
print ("File opened successfully!!")

