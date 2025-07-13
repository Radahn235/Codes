for i in range(1,6):
    for j in range(i-1):  #for spaces
        print(" ",end=" ")
    for k in range(2 * (5 - i) + 1): # for*
            print("*",end=" ")
    print()    

