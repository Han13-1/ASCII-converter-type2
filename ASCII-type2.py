i=0
while i< 1:
    x = input("insert your value: ")
    if x.isalpha():
        print("your character is: ",ord(x))
    elif int(x) in range(0,9):
        n = input("is this an ASCII value? yes or no:  ")
        if n == "yes":
            print("your character is: ", ord(x))
        elif n == "no":
            y= int (x)
            print(f'the ASCII value of {y} is: ',chr(y))
    elif int(x) in range(10,110000):
        y = int(x)
        print(f'the ASCII value of {y} is: ',chr(y))