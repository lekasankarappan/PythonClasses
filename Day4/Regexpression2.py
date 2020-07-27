import re

txt="The rain in spain"
x=re.split("\s",txt)# \s returns a match where the string contains the white space
print(x)
print(len(txt))# returns with totalno of charactersincliuding spaces
print(len(x))