txt = input() #take user input string

array = txt.split() #make that string into array form
fake = [] #will be used by adding elements

#lets get biggest length of arrays by using max()

for a in range(len(array)):
    length = len(array[a])
    fake.append(length)
    
value = max(fake)

#now we need index number so that we can access that word which is bigger

for i in range(len(fake)):
    if(fake[i] == value):
        result = i
        
#finally print that word

print(array[result])
    
