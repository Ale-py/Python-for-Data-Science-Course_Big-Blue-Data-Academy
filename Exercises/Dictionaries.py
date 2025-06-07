# 1. Create a dictionary named person with keys "name", "age", and "city" and
# assign them values (e.g., "Alice", 30, and "New York"). Then, print the dictionary.
person = {
    "name" : "Alice",
    "age" : 30,
    "city" : "New York"
}
print(person)
# 2. Given the dictionary person = {"name": "Alice", "age": 30, "city": "New York"}, print the value associated with the key "age".
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
    }

print(person["age"])
# 3. Start with the dictionary fruit_colors = {"apple": "red", "banana": "yellow"}.
# Add a new key "grape" with the value "purple" and then print the updated dictionary.
fruit_colors = {
    "apple": "red",
    "banana": "yellow"
    }
fruit_colors["grape"] = "purple"
print(fruit_colors)
# 4. Using the dictionary person = {"name": "Alice", "age": 30, "city": "New York"}, 
# update the value of "age" to 31 and print the modified dictionary.
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
    }
person["age"] = 31
#person.update({"age":"31"})
print(person)
# 5. Given the dictionary person = {"name": "Alice", "age": 30, "city": "New York"}, 
# remove the key "city" using the pop() method and print the updated dictionary.
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
    }
person.pop("city")
print(person)
# 6. With the dictionary person = {"name": "Alice", "age": 30, "city": "New York"}, 
# write a loop that iterates over the dictionary and prints each key along with its corresponding value.
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
    }
for key,value in person.items():
    print(f"{key}: {value}")




