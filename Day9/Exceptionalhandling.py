i=12
j=0

print("starting")

try:
    print(i/j)
except FileNotFoundError:
    print("Number can't be divide by zero")

except ZeroDivisionError :
    print("Number can't be divide by zero")
print("Ending")
