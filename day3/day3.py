import numpy as np

def enum(**enums):
    return type('Enum', (), enums)

Directions = enum(NORTH='^', SOUTH='v', EAST='>', WEST='<')



 
def readFile(file):  
    i=0 
    
    with open(file, 'r') as f:
        for line in f:
            for c in line:
                i+=1
        print(i)




readFile("instructions.txt")

