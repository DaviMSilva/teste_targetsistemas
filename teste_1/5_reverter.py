def revertString(string):
    lenString = len(string)
    newString =''
    while(lenString > 0):
        lenString-=1
        newString+=string[lenString]
    
    return newString
       

print(revertString('maria'))