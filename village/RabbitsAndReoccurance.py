def Fibonannci_Loop_Pythonic(months, offsprings):
    parent, child = 1, 1
    for itr in range(months -1):
        child, parent = parent, parent + (child * offsprings)
    return child

print(Fibonannci_Loop_Pythonic(5, 3 ))