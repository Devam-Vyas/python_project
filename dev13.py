colors = ['Red', 'Black', 'Green']
print('Original List:', colors)

# change the first item to 'Purple'
colors[2] = 'Purple'

# change the third item to 'Blue'
colors[2] = 'Blue'

print('Updated List:', colors)
numbers = [2,4,7,9]

# remove 4 from the list
numbers.remove(4)

print(numbers)
names = ['John', 'Eva', 'Laura', 'Nick', 'Jack']

# delete the item at index 1
del names[1]
print(names)

# delete items from index 1 to index 2
del names[1: 3]
print(names)

# delete the entire list
del names

# Error! List doesn't exist.
print(names)

