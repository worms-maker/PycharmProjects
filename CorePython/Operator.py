# Arithmetic operator
upper = 10
lower = 50

print("Addition", upper + lower)
print("Multiplication", upper * lower)
print("Exponent", upper ** 2)
print("Float Division", lower / upper)  # Division (Float) Return Float Value
print("Floor Division", lower // upper)  # Division (Floor) Return Floor Value
print("Subtraction", lower - upper)
print("Modulus", upper % lower)

# Comparision Operator & also use in String Comparision
less = 44
grater = 66

print('GraterThan ', less > grater)
print('LessThan', grater < less)
print('GraterEqual', less >= grater)
print('LessEqual', grater <= less)
print('Not Equal', less != grater)
print('EqualEqual', less == grater)

# Assignment Operator
left = 3
right = 3

left += right
print('+=', left)
left **= right
print('**=', left)
left -= right
print('-=', left)
left *= right
print('*= ', left)
left /= right
print('/=', left)
left //= right
print('//=', left)
left %= right
print('%=', left)

left = 3
right = 2
left &= right
print('&=', left)
left |= right
print('|=', left)
left ^= right
print('^=', left)
left >>= right
print('>>>', left)
left <<= right
print('<<<', left)

# Logical Operator
left = True
right = False
print(left and right)
print(left or right)
print(not left)

# Bitwise Operator
left = 4
right = 10
print('Bitwise OR', left | right)
print('Bitwise AND', left & right)
print('Bitwise XOR', left ^ right)
print('Bitwise NOT', ~ right)
print('Left Shift', left << 2)
print('Right Shift', left >> 2)

# Identity Operator
A = 1
B = 1
A_A = 'Python'
B_B = 'Python'
A_A_A = [34, 34, 34]
B_B_B = [34, 34, 34]
print(A is not B)
print(A_A is B_B)
print(A_A_A is B_B_B)

# MemberShip Operator
list = [23, 45, 67]
print(23 in list)
print(44 not in list)

                                            # Amazing Facts About Python
                                            #  - IN Bitwise not operator Internally Perform 2's Compliment
                                            #  - is, is not operator
                                            #  - in , not in operator

