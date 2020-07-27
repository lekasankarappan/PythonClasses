import re

otp="Hi leka 232332 is your otp "\
    "completing the txn  your"\
    "account no .242342342"
value=re.search("\d{6}",otp)
print(value)