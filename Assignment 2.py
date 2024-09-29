# Exercise (1)  
# 
# def getFactorial(n):
# 
    # factorial = 1
    # if n > 0:
# 
        # for i in range(1,n+1):
            # factorial *= i
# 
# 
        # print(factorial)
# 
# 
# 
    # else:
        # print("please insert a postive number") 
# 
# 
# getFactorial(int(input("please enter a positive number: ")))   
# 


# Exercise (2)


# def getDivisors(n):
#    
    # list1=[]
    # i = 1
    # while(i <= n):
        # if (n % i == 0):
            # list1.append(i)
            # 
        # i += 1
        # 
    # print(list1)
# 
# getDivisors(n = int(input("please enter a number: ")))



# Exercise (3)

# 
# def reverseString(n):
# 
    # i = len(n)
    # 
    # while (i > 0):
# 
        # i -= 1
        # print(n[i],end="")
# 
# 
# reverseString((input("please enter a string: ")))



# Exercise (4)

# 
# user_input = input("please enter your numbers comma separated: ")
# 
# list = user_input.split(',')
# even_list = []
# 
# for i in range(len(list)):
    # if int(list[i]) % 2 == 0:
        # even_list.append(int(list[i]))
# 
# print(even_list)
# 

# Exercise (5)

# pass_entered = input("please enter your password: ")
# 
# has_upper = False
# has_lower = False
# has_digit = False
# has_special = False
# pass_isLong = False
# special_list =  ["#","?","!","$"]
# 
# 
# for i in range(len(pass_entered)):
        # 
    # if (pass_entered[i].isupper()):
        # has_upper = True
# 
    # if (pass_entered[i].islower()):
        # has_lower = True
# 
# 
    # if (pass_entered[i].isdigit()):
        # has_digit = True
# 
    # if (pass_entered[i] in special_list):
        # has_special = True
# 
# if len(pass_entered) >= 8:
    # pass_isLong = True
# 
# 
# if ((has_digit and has_lower and has_special and has_upper and pass_isLong) == True):
    # print("Strong Password")
# 
# else:
    # print("Weak Password")
# 


# Exercise (6)


# address = input("please enter your IPv4 address: ")
# 
# address = address.split(".")
# 
# i = 0
# valid_ip = True
# 
# while(i < len(address)):
    # if (int(address[i]) >= 255):
        # valid_ip = False
        # break
    # i+=1
# 
# if valid_ip:
    # print("IPv4 address is valid")
# 
# else:
    # print("IPv4 address is invalid")


    
   









    







           



