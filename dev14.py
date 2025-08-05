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
cars = ['BMW', 'Mercedes', 'Tesla']

print('Total Elements:', len(cars))
fruits = ['apple', 'banana', 'orange']

# iterate through the list
for fruit in fruits:
    print(fruit)
