# Declaration of Variable in Python
# Python Work with Indentation so, When Write code Then Most important is Formatting of Code.

# Python Variable name Only Start With (_)UnderScore or Alphabets.
# Other Keyboard Symbols are Not accept in NamingConvention.

# Use Different Type of Case
# (1). PascalCase : NameOfSchool
# (2). camelCase  : getDataOfTable
# (3). Snake Case : name_of_laptop
from wsgiref import validate

A = 10
B = 15
B_A = 20
_A = 30
B_ = 40
print(A, B, B_A, _A, B_)  # 10 15 20 30 40

# Internally Work of Python for Assigning Variable
# id() return the
X = 10
Y = X
print("X :", id(X))
print("Y :", id(Y))
# both Variable Id same

X = 12
print("X :", id(X))  # X id is Different SO, Create New Object When Declare Again

# Assign One Value to Multiple Variable
E = F = G = 100
print(E, F, G)

# Assign Multiple Value to Multiple Variable
H, I, J = 12, 23, 34
print(H, I, J)

# type() method Return's Type of Object
name = "First Learn then Remove 'L'"
print("NameType :", type(name))
float_A = 1.1
print("float_A_Type :", type(float_A))

# Amazing Facts About Python Variable
#  - In Python No any Keyword Use like : Integer , String , boolean etc.
#  - Just Write Variable name and assign it's Value


