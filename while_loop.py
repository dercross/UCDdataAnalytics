#error = 1000
#while error > 1:
    #error = error / 4
    #print("Cal_error")
    #print(error)

# Initialize offset
offset = -6

# Code the while loop
while offset != 0 :
    print("correcting...")
    if offset > 0:
        offset = offset - 1
    else:
        offset = offset + 1
    print(offset)
