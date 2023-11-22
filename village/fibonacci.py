def Fiboncci_Loop(number):
    old = 1
    new = 1
    for itr in range(number - 1):
        tmpVal = new
        new = old
        old = old + tmpVal
    return new


def Fibonannci_Loop_Pythonic(number):
    old, new = 1, 1
    for itr in range(number -1):
        new, old = old, new + old
    return new

print(Fiboncci_Loop(10)) 

