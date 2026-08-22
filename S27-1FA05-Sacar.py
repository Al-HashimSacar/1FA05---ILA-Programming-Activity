# Reflection:
# Using a library is more practical because it provides pre-built, highly optimized 
# functions like sqrt() and pow(), saving time and reducing potential calculation errors. 
# Without the math library, calculating complex operations like square roots from scratch 
# would require writing custom algorithms, making the program longer and much harder to maintain.

import math

# Prompt the user to input coordinates
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Calculate distance using Euclidean distance formula: sqrt((x2 - x1)^2 + (y2 - y1)^2)
distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

# Display result
print(f"The distance between ({x1}, {y1}) and ({x2}, {y2}) is: {distance:.2f}")