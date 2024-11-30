#Lists should all the values of the same data ype
#can be extended or shrinked
# 0   2  3  4 --index number
#1  , 6 ,8 9  , 0
#-5 -4 -3 -2   -1 --negative indexing

nums = [2 , 4 , 7 , 9 , 9 , 8 , 7 , 6 , 3]

print(nums[5])

print(nums[-2])

names = ['Hayyan' , 'Rayyan' , 'Fatima' , ' Areeb' , 'Ibrahim']
print(names[3])

values = ['Hassan' , 3 , 6.5 , True]
print(values)

print("-------------------------------------------------------")

check = [nums , names]
print("COMBINED LIST")
print(check)

nums.insert(2,77)
print("INSERT")
print(nums)

names.append("Hayyan")
print("APPEND")
print(names)

nums.extend([24,66,76,45,43])
print(nums)

nums.remove(8)
print(nums)

nums.pop(1)
print(nums)

nums.pop()
print(nums)

del names[3: ]
print(names)

nums.extend([45,66,76,45,43])
print(nums)

print("Smallest number :" , min(nums))
print("Largest number :" , max(nums))
print("Sum = " , sum(nums))

nums.sort()
print(nums)
print(nums[4])

names.sort()
print(names)

nums.sort(reverse = True)
print(nums)

names.sort(reverse = True)
print(names)

name_copy = names.copy()
print(name_copy)

join_list = names + nums
print(join_list)

index_name = names.index("Rayyan")
print(index_name)

print(nums.count[7])

fruits = ["apple", "banana", "cherry", "date"]

fruits.append("elderberry")
fruits.insert(1, "blueberry")

fruits.remove("banana")
removed_fruit = fruits.pop() # Remove the last iten and get it

#4 accessing elements in the list
print("First Fruit: ", fruits[0])
print("Last fruit: ", fruits[-1])

#Iterating through the list
print("Current fruits in the list: ")
for fruit in fruits:
    print(fruit)

print("Number of fruits: ", len(fruits))

if "cherry" in fruits:
    print("Cherry is in the list")
else:
    print("Cherry is not in the list")

print("Final list of fruits:", fruits)