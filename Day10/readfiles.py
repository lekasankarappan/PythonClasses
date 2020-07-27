# D:\\myfile\\welcome\\data.txt
#D:\\data.txt

#file_object=open("filename+path","accessmethod")
file = open("data.txt",'r')
print(file.read())
#to print each line
#file.readline(5)-.it will return with first 5 letters
print(file.readline())

