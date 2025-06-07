# 1. Create a list named fruits that contains the following elements: "apple", "banana", and "cherry". Then, print the list.
fruits = ["apple","banana","cherry"]
print(fruits)
# 2. Start with an empty list called numbers. Append the integers 1, 2, and 3 to the list, and then print it.
numbers = []
numbers.append(1)
numbers.append(2)
numbers.append(3)
print(numbers)
# 3. Given the list colors = ["red", "green", "blue"], print the first element and the last element using indexing.
colors = ["red", "green", "blue"]
print(colors[0],colors[-1])
# 4. Use the list letters = ["a", "b", "c", "d", "e"] and slice it to create
# a new list that contains elements from index 1 to 3 (inclusive of index 1 but excluding index 4). Print the new list.
letters = ["a", "b", "c", "d", "e"]
newList = letters[1:3]
print(newList)
# 5. Create a list animals = ["cat", "dog", "rabbit", "horse"]. Use the len() function to print the number of elements in the list.
animals = ["cat", "dog", "rabbit", "horse"]
print(len(animals))
# 6. Create two lists, list1 = [1, 2, 3] and list2 = [4, 5, 6]. Concatenate them into a new list called combined_list and print it.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
#list1.extend(list2)
#print(list1)
print(combined_list)
# 7. Given the list numbers = [10, 20, 30, 40, 50], remove the element 30 using the remove() method and then print the updated list.
numbers = [10, 20, 30, 40, 50]
numbers.remove(30)
print(numbers)















