# Python Bitwise Operators take one to two operands, and operates on it/them bit by bit, instead of whole.

# Bitwise AND (&) Operator
# Sets each bit to 1 if both bits are 1

# 0 & 0 -> 0
# 0 & 1 -> 0
# 1 & 0 -> 0
# 1 & 1 -> 1

print(5 & 7)

# Bitwise OR ( | ) Operator
# Sets each bit to 1 if one of two bits is 1

# 0 | 0 -> 0
# 0 | 1 -> 1
# 1 | 0 -> 1
# 1 | 1 -> 1

print(5 | 7)

# Bitwise XOR ( ^ ) Operator	
# Sets each bit to 1 if only one of two bits is 1

# 0 ^ 0 -> 0
# 0 ^ 1 -> 1
# 1 ^ 0 -> 1
# 1 ^ 1 -> 0

print( 5 ^ 8)

# Bitwise NOT ( ~ ) Operator 
# Inverts all the bits

#  ~ 0 -> 1
#  ~ 1 -> 0

print(~66)

# Bitwise Left Shift ( << ) Operator
# Shift left by pushing zeros in from the right and let the leftmost bits fall off

print(6<<2)

# Bitwise Right Shift ( >> ) Operator	
# Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

print(6>>2)