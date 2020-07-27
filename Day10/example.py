from faker import name,internet

def fullName():
    fn = name.first_name()
    ln = name.last_name()
    fl = fn +" "+ ln
    return fl

def email():
    email =str(fullName()).replace(" ","_")+"@testmail.com"
    return email

print(email())