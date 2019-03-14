doc = open('rosalind_hamm.txt','r').read().splitlines() #This is to read the file and split the 2 lines into 2 items in a list called doc.
count = 0 #Declare a value for count, so we add value to it.

for a,b in zip(doc[0], doc[1]): #A loop goes through each item that is created from zipping line 0 and line 1 togther.
    if a!=b: # in each item, if a is not equal to b, then add 1 to count
        count+=1
print count # this is to globally print out the count of total number of a not equal to b
