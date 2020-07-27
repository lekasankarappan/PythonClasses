import math

while True:
    print("\nchoose the operation.\n\n1.Adddition.\n2.Subtraction\n3.multiplication.\n4.Division\n5.molules"+"\n")

    oper=input("\n your option for the menu"+"\n")

    if oper=="1":
       val1 = float(input("\nEnter the first number:"))
       val2 = float(input("\nEnter the second number:"))

       print("\n the result is:"+str(val1+val2)+"\n")
       back= input("Go back to the main menu?(Y/N)\n")
       if back == 'y':
         continue
       else:
         break
    elif oper=="2":
       val1 = float(input("\nEnter the first number:"))
       val2 = float(input("\nEnter the second number:"))

       print("\n the result is:"+str(val1-val2)+"\n")
       back= input("Go back to the main menu?(Y/N)\n")
       if back == 'y':
         continue
       else:
         break

    elif oper == "3":
       val1 = float(input("\nEnter the first number:"))
       val2 = float(input("\nEnter the second number:"))

       print("\n the result is:" + str(val1*val2) + "\n")
       back = input("Go back to the main menu?(Y/N)\n")
       if back == 'y':
         continue
       else:
         break
    elif oper == "4":
        val1 = float(input("\nEnter the first number:"))
        val2 = float(input("\nEnter the second number:"))

        print("\n the result is:" + str(val1 / val2) + "\n")
        back = input("Go back to the main menu?(Y/N)\n")
        if back == 'y':
          continue
        else:
          break
    elif oper == "5":
        val1 = float(input("\nEnter the first number:"))
        val2 = float(input("\nEnter the second number:"))

        print("\n the result is:" + str(val1 % val2) + "\n")
        back = input("Go back to the main menu?(Y/N)\n")
        if back == 'y':
           continue
        else:
           break
