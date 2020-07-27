#pop(),remove(),c;lear()
oldlist=["Arvind","Neel","leka","Raja"]
newlist=["Rana","Kumar","Xhi","Trump"]
list=[1,2,3,4,5]
newlist=oldlist.copy()
print(newlist)
print(oldlist)
print(list[0:])
newlist=list[:]
print(newlist)
for z in zip(oldlist,newlist):
    print(z)