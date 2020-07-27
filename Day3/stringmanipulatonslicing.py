#syntax for slicing
#str_obj[start:end:step]
#<-- -7,-6,-5,-4,-3,-2,-1 backward
v="youtube"
#-->0,1,2,3,4,5,6,7 forward
print(v[-4])
print(v[3])
#to automatically print from start to end
print(v[:])

print(v[0:3])
print(v[-7:-4])
print(v[::-1])