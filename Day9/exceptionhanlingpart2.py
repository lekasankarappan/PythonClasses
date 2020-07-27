i=12
j=0

print("starting")

try:
    print(i/j)
except :
    print("Exception handled")
    raise
finally:
    print("closing connection")
    
print("Ending")
