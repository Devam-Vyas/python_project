fruits = ['apple', 'banana', 'orange']
print('Original List:', fruits)

fruits.append('cherry')

print('Updated List:', fruits)
fruits = ['apple', 'banana', 'orange']
print("Original List:", fruits) 

fruits.insert(2, 'cherry')

print("Updated List:", fruits)
numbers = [1, 3, 5]
print('Numbers:', numbers)

even_numbers  = [2, 4, 6]
print('Even numbers:', numbers)

# adding elements of one list to another
numbers.extend(even_numbers)

print('Updated Numbers:', numbers) 
