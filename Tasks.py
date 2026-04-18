# List Task - Basic Operations on Lists in Python

# 1. Create a list of numbers
my_list = [5, 10, 15, 20, 25]

# 2. Print the first element
print("First element:", my_list[0])

# 3. Print the last element
print("Last element:", my_list[-1])

# 4. Use a for loop to print all elements
print("All elements:")
for item in my_list:
    print(item)

# 5. Print only numbers greater than 10
print("Numbers greater than 10:")
for item in my_list:
    if item > 10:
        print(item)