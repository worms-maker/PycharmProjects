""" Python DataType Hold the Value of variable. We don't define the Type of variable in .py file.
Interpreter automatically  binds type of Variables. """

"""Strings in Python"""

# String DataType
single_quotes = 'Python String with Single Quotes'
double_quotes = "python string with double quotes"
triple_quotes = '''PYTHON String with Triple Quotes'''

print(single_quotes)
print(double_quotes)
print(triple_quotes)  # Triple Quotes Allow Multiple Line String

'''
 0    1   2    3    4   5    6   7    8    9   10   11
--------------------------------------------------------:
 P    y   t    h    o   n    S   t    r    i    n    g  :       <-- Python String
--------------------------------------------------------:
-12 -11  -10  -9   -8   -7  -6  -5   -4   -3   -2   -1 
'''

"""Access the String ans also get SubString"""
print(single_quotes[1])  # 'y' Positive then First number Index
print(single_quotes[-1])  # 's' Negative Then Last  number Index
print(single_quotes[0:4])  # 0 include and 4 exclude

"""Update and Deletion of String is not supported Because String is Immutable in Python"""
# string_double_quotes[2] = "2"                        <-- Try to Replace String  (Not Supported)
# del string_double_quotes[3]                          <-- Deletion from String  (Not Supported)
print(double_quotes.replace("Python", "java"))         # Possible using Replace Method of String.

"""if we write Path and quoted String then Use Prefix  'r' = rawString"""
"""link : 'https://docs.python.org/3/reference/lexical_analysis.html#strings'"""
print(r"c:\user\root\kit")

"""If we want to Concatenation of two String then"""
print("python ""best")

"""String Methods"""
print(len(single_quotes))
print(single_quotes.replace('P', 'J'))
print(double_quotes.capitalize())         # First Latter Capital All other Small
print(triple_quotes.casefold())           # Return CaseLess String
print(single_quotes.rjust(44, "#"))       # Right Justify
print(single_quotes.ljust(45))            # Left Justify
print('python '.isalpha())                # false , Contain WhiteSpace
print('123'.isnumeric())                  # true , String numeric

"""https://docs.python.org/3.8/library/stdtypes.html#str.casefold"""


# Amazing Facts About Python String
#  - Concatenation of two String  simply Write ('ABC' 'DEF') no any operator use.
