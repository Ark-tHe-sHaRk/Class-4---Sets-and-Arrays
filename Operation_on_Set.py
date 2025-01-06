#Printing a set
my_set = {1, 2, 3}
print(my_set)
#Printing a set with multiple data types ## Notice the order is different: string, float, integer.  
my_set1 = {1.0, 'hello', (1, 2, 3)}
print(my_set1)
#A set with duplicate values ## Notice the values are being pasted once in the output even multiple are present 
my_set2 = {1, 2, 3, 4, 1, 2, 3, 4, 3, 3, 3, 5}
print(my_set2)
#Making a set with a list, If you add the word set before the paranthesis it will print as a set. 
my_set3 = ([1, 2, 3, 4, 5, 6, 7])
print(my_set3)
#Removing an element from an set 
my_set4 = {1.0, 2.3, 2}
my_set4.pop()
print(my_set4)

