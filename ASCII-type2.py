i=0
while i< 1:
    x = input("insert your value: ")
#get ASCII    
    if x.isalpha():
        print("your character is: ",ord(x))
#differencial        
    elif int(x) in range(0,9):
        n = input("is this an ASCII value? yes or no:  ")
        if n == "yes":
            print("your character is: ", ord(x))
        elif n == "no":
            y= int (x)
            print(f'the ASCII value of {y} is: ',chr(y))
#deliver ASCII            
    elif int(x) in range(10,109999):
        y = int(x)
        print(f'the ASCII value of {y} is:',chr(y))
#unexistant
    elif int(x) in range(110000,99999999999999999999999999999999999999):
        print("anything x>=109999 hasn\'t got an assigned value")
#(couldn't find how to make +infinity)
