s1 = "Hello"
s2 = 'Python'
s3 = """Welcome  to string demo"""

print("Length of s3:", len(s3))
print("Length of s3:", len(s3+s2))
print("Length of s3:", len(s3-s2))
print("Length of s3:", len(s3)+len(s2))

#OUTPUT

Length of s3: 23
Length of s3: 29
ERROR!
Traceback (most recent call last):
  File "<main.py>", line 7, in <module>
TypeError: unsupported operand type(s) for -: 'str' and 'str'

=== Code Exited With Errors ===
