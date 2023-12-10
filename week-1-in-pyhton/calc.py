# Floating-point imprecision

# Prompt user for x
x = int(input("x: "))

# Prompt user for y
y = int(input("y: "))

# Divide x by y
z = x / y
#if you want a cereten number afte rthe decimal place in a f string put :. then number of digets you want after the decimal and "f": example .50f
print(f"{z:.50f}")
