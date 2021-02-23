# Open a file: file
with open('import_text.txt' , 'r') as file:

# Print it
 print(file.read())

# Check whether file is closed
print(file.closed)

# Close file
file.close()

# Check whether file is closed

print(file.closed)

