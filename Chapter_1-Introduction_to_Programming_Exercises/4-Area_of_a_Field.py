# Create a program that reads the length and width 
# of a farmer’s field from the user in feet. 
# Display the area of the field in acres.

width = float(input("Width of the field: "))
length  = float(input("Length of the field: "))

area_feet = width * length
area_acres = area_acres = area_feet / 43.560

print("The area of the field in acres is:", area_acres)