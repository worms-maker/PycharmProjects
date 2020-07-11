# here all Possible method to Develop Python Swapping Code.
# in the Python Swapping value of All the DataTypes
# Here Develop Code on Swapping Continue..

x = 10;
y = 5;

# by using Python Simple Method

print(x, y)
x, y = x, y
print(x, y)

print("\nPython Swap x :", x)
print("Python Swap x :", y)
# By Using XOR Approach

x = x ^ y
y = x ^ y
x = x ^ y

print("\nXOR-Value of x:", x)
print("XOR-Value of y:", y)

# By Using + Operator

x = x + y
y = x - y
x = x - y

print("\n+ Value of x:", x)
print("+ Value of y:", y)

# By Using Temp Variable

temp = x
x = y
y = temp

print("\nTemp Value of x:", x)
print("Temp Value of y:", y)
