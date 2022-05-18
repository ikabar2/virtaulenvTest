from ast import pattern
import re
import keyword


var1 = input()
#pattern = r^'[a-zA-Z_]\w*$'


if (var1.isidentifier()):
    print(var1 + "  is valid")

else:
    print(" not valid")