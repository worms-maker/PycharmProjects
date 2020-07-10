# Here Perform the Python number and Mathametics in Python
# Here Use the 'type()' function for get Variables type.

# Get the Type of Variable or Which Variable belong to Which Class (No Size)
x = 4;
print(type(x))

# Floating point Number Accurate with 15 Decimal Point 16th place is Unaccurate
y = 4.00
print(type(y))

# Addition of 2 Complex Number
c = 5 + 3j
z = c + 3 + 4j
print(z)
print(isinstance(z, complex))

print('\n')

# Perform the Digital Number Format in Python and Also Formatting in String with Python
print(20 * '--')
print("| {}".format("Number Format" + 8 * ' ') + "{} |".format('Prefix' + 8 * ' '))
print(20 * '--')
print("| Binary" + 15 * ' ' + "{}".format('0b : 0B' + 8 * ' ' + '|'))
print("| Octal" + 16 * ' ' + "{}".format('0o : 0O' + 8 * ' ' + '|'))
print("| Hexa-Decimal" + 9 * ' ' + "{}".format('0x : 0X' + 8 * ' ' + '|'))
print(20 * '--')
print('Perform the Digital Number')

print('Binary : ', 0b0001, 0B0010)
print('Octal : ', 0o100, 0O1000)
print('Hexa-Decimal', 0X0001, 0XF)

print('\nHere Use the Place Holder In Python')
print('Int : %2.3d , Float : %2.3f ' % (1, 2.2))

print("i am {name} {a:4.4f}".format(name='darshan', a=8.0))

"""
<   :  left-align text in the field
^   :  center text in the field
>   :  right-align text in the field
"""

discription = "my name is Malware"
print("\n\nnow Perform Justify in Python")
print(discription.center(40, " "))
print(discription.ljust(40, " "))
print(discription.rjust(40, " "))


#print("{:*^name}".format(name='darshan'))
