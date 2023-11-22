import this


variables
import math
def tri(a,b):
    hypotenuse = a**2 + b**2
    return hypotenuse 
a = 3
b = 5
result= tri(a,b)
print(result)

def slice_string(s, a, b, c, d):
    if a < 0 or b >= len(s) or c < 0 or d >= len(s) or a > b or c > d:
        return "Invalid input indices"
    
    slice1 = s[a : b + 1]  # Include b in the slice
    slice2 = s[c : d + 1]  # Include d in the slice
    
    return slice1 + " " + slice2

# Example usage:
input_string = "HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain."
a = 22
b = 27
c = 97
d = 102
result = slice_string(input_string, a, b, c, d)
print(result)

start = 100
end = 200
result = 0

for x in range (start, end + 1):
    if x % 2 != 0:
        result += x
print (result)

outputFile = []

with open ('village/input.txt', 'r') as f:
    outputFile = [line for pos, line in enumerate(
        f.readlines()) if pos % 2 !=0]

with open ('village/out.txt', 'w') as f:
    f.write(''.join((line for line in outputFile)))

txtStr = "We tried list and we tried dicts also we tried Zen"
wordCountDict = {}

for word in txtStr.split(' '):


    if word in wordCountDict:
        wordCountDict[word] += 1
    else:
        wordCountDict[word] = 1

for key, value in wordCountDict.items():
    print(key, value)



