# Day 10 - list comprehensions

# Traditional way to filter a list
numbers = [3, 7, 10, 15, 20]
filtered = []

for n in numbers:
    if n >= 10:
        filtered.append(n)
print(filtered)

print("-----")

# Using list comprehension to filter a list
numbers = [3, 7, 10, 15, 20]
filtered = [n for n in numbers if n >= 10]
print(filtered)

print("-----")

# Using list comprehension to create a new list with word lengths
words = ["apple", "car", "cherry", "dog"]
long_words = [w for w in words if len(w) > 3]

print(long_words)

print("-----")

orders = [1200, 0, -300, 4500, "error", 2300, None, 800]
valid_orders = [o for o in orders if type(o) == int and o > 0]
print(valid_orders)
