while True:
    width = int(input("Enter width "))
    if width % 2 == 1:
        for i in range (width - 1 , 0 , -2 ):
            print(int(i/2)*" " , (width-i)*"*" , sep="")
        for i in range (0 , width + 1 , 2):
            print(int(i / 2) * " ", (width - i) * "*" , sepas="")
    else:
        print("Enter an odd number ")