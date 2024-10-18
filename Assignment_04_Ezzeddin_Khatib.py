def menU():
    choice = 0
    print("1.Sum Tuples")
    print(" ")
    print("2.Export JSON")
    print(" ")
    print("3.Import JSON")
    print(" ")
    print("4. Exit")
    print(" ")
    print("- - - - - - - - - - - - - - -")
    print(" ")
    n = int(input("Enter a Choice: "))
    return n
def selecT():
    n = menU()
    if n == 1:
        choice = 1
    elif n == 2:
        choice = 2
    elif n == 3:
        choice = 3
    elif n == 4:
        choice = 4
    return choice
##### Choice 1 #####
def addTuples(tup1,tup2):
    x=0
    tups1 = list(tup1)
    tups2 = list(tup2)
    n = len(tups1)
    m = len(tups2)
    sums = []
    if n == m: 
        for i in range(n):
            x = int(tups1[i])+int(tups2[i])
            sums.append(x)
        tups = tuple(sums)
        return tups
    else:
        print("can't add tuples of different lengths!")
##### Choice 2 #####
def dicttojson(dict1,filename):
    
    file= open(filename,'w') 
    file.write("{\n")
    items = [] 
    for key,value in dict1.items():
        keys = f'"{key}"' 
        
        if isinstance(value,str): 
            value_s = f'"{value}"'
        elif isinstance(value,(int,float)):
            value_s = str(value) 
        elif isinstance(value,bool):
            value_s = str(value).lower() 
        elif value is None:
            value_s = 'null' 
        items.append(f" {keys} : {value_s}")
    file.write(",\n".join(items)) 
    file.write("\n}")
###### Choice 3 ######

def jsontopython(filename):
    
    file=open(filename, 'r') 
    j_s = file.read().strip()

    j_s = j_s[1:-1].strip()

    result = []
    
    obj = ""
    open_braces = 0

    for char in j_s:
        obj += char
        
        if char == '{':
            open_braces += 1
        elif char == '}':
            open_braces -= 1
        
        if open_braces == 0 and obj:
            dict1 = {}
            obj = obj.strip()[1:-1]  
            pairs = obj.split(',')  #
            
            for p in pairs:
                if ':' in p:
                    keys = p.split(':', 1)
                    key = keys[0].strip().strip('"') 
                    
                    
                    value = keys[1].strip()
                    if value.startswith('"') and value.endswith('"'):
                        value = value[1:-1]  
                    elif value == "true":
                        value = True
                    elif value == "false":
                        value = False
                    elif value == "null":
                        value = None
                    else:
                        try:
                            value = int(value)
                        except ValueError:
                            try:
                                value = float(value)
                            except ValueError:
                                pass
                    
                    dict1[key] = value
            
            result.append(dict1)
            obj = ""  

    return result

###### Choice 4 ######
def exitS():
    print("The program will stop now!")
    quit()
########################################################################
#the function that calls functions from the above according to each choice:
def chooSe():
    choice = selecT()
    if choice == 1:
        input1 = input("Enter elements of the first tuple separated by space or commas: ")
        tuple1 = tuple(input1.replace(',', ' ').split())
        input2 = input("Enter elements of the second tuple separated by space or commas: ")
        tuple2 = tuple(input2.replace(',', ' ').split())
        print ("the sum of elements of both tuples is: ",addTuples(tuple1,tuple2)) 
        chooSe()
    elif choice == 2:
        newdict = {}
        print("\n")
        n=int(input("enter number of students: "))
        for i in range(n):
            key = input("enter name of the student: ")
            value= float(input("enter score: "))
            newdict.update({key: value})
        filename=input("input the name of a .json file: ")
        print(dicttojson(newdict,filename))
        print("done! check file")
        print("\n\n")
        chooSe()
    elif choice == 3:
        filename = input("enter the name of the json file: ")
        print(jsontopython(filename))
        print("\n\n")
        chooSe()
    elif choice == 4:
        exitS()
######main function#######
def main():
    chooSe()
if __name__ == "__main__":
    main()
















