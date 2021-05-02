import sys#, imp, json, traceback, time, socket, math

try: 
    if len(sys.argv) > 1:
        inputList = sys.argv[1:]
    else:
        print("Missing input")
        print("Please enter your command in this format: python main.py 23 34")
        sys.exit(0)

    for i in range(len(inputList)):
    
        remainder = []
        
        # calcute remainder and quotient
        inputListInt = int(inputList[i])
        rem = inputListInt % 10
        #print(rem)
        remainder.append(rem)
        quot = int(inputListInt / 10)
        #print(quot)

        # calcute remainder and quotient recursively
        while quot >= 1:
            rem = quot % 10
            remainder.append(rem)
            quot = int(quot / 10)
            #print(quot)
    
        #print(remainder)
        for j in reversed(remainder):
            if j == 1:
                print("One", end="")
            elif j == 2:
                print("Two", end="")
            elif j == 3:
                print("Three", end="")
            elif j == 4:
                print("Four", end="")
            elif j == 5:
                print("Five", end="")
            elif j == 6:
                print("Six", end="")
            elif j == 7:
                print("Seven", end="")
            elif j == 8:
                print("Eight", end="")
            elif j == 9:
                print("Nine", end="")
            elif j == 0:
                print("Zero", end="")
            else:
                print("NA", end="")

        if i < len(inputList)-1:
            print(",", end="")
        else:
            print("")

except Exception as ex:
    print("error")


