
Name=[]
file=open("List.txt",'w+')

for X in range(0,10):

  Name.append(input("Enter ur name:"))
file.write(str(Name))
file.close()

  #print(Name)
#print(list(ra