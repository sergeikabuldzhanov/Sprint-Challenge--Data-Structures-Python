from binary_search_tree import BinarySearchTree
import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# Initial runtime complexity is O(n^2)
bst = BinarySearchTree(names_1[0])
# Complexity of O(n*log(n))
for i in range(1, len(names_1)):
    bst.insert(names_1[i])
# Complexity of  O(n*log(n))
for name in names_2:
    if bst.contains(name):
        duplicates.append(name)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

# 1. Using 2 sets O(n) and set.intersection
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = list(set(names_1).intersection(set(names_2)))


end_time = time.time()
# print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"Sets intersection runtime: {end_time - start_time} seconds")


# Sorting the list and using a while loop. O(nlog(n))
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


def find_duplicates(a, b):
    """
    Takes 2 sorted lists as input, yields every duplicate value found
    If wrapped in a function creating an iterable, will create that iterable
    """
    i = 0
    j = 0
    # Traverse both lists at the same time, done when we finish either one
    while i < len(a) and j < len(b):
        # compare values, increment the appropriate pointer, since lists are sorted, this will find us duplicates
        if a[i] > b[j]:
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            # if values are equal, yield the value, increment both pointers
            yield a[i] # yield allows us to treat this as an iterable
            j += 1
            i += 1


duplicates = list(find_duplicates(sorted(names_1), sorted(names_2)))

end_time = time.time()
# print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"Intersect function on sorted lists, O(n*log(n)+n): {end_time - start_time} seconds")


# Using intermediate set. O(n)
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

temp = set(names_1)
duplicates = [name for name in names_2 if name in temp]

end_time = time.time()
# print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"1 set and a for loop runtime: {end_time - start_time} seconds")


# Dictionary and for loops
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
unique = {}
for name in names_1:
    unique[name] = None
for name in names_2:
    if name in unique:
        duplicates.append(name)


end_time = time.time()
# print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"Dictioinary and for loops runtime: {end_time - start_time} seconds")

# 2 sets and bitwise operator
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()
set1 = set(names_1)
set2 = set(names_2)
duplicates = list(set1 & set2)


end_time = time.time()
# print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"Two sets and bitwise operator: {end_time - start_time} seconds")

# Filter function and a lambda
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = list(filter(lambda x: True if x in names_2 else False, names_1))


end_time = time.time()
# print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"Filter and a lambda: {end_time - start_time} seconds")

# Casual list comprehension O(n^2), but is still faster than the default for some reason.
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = [name for name in names_1 if name in names_2]


end_time = time.time()
# print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"List comprehension runtime: {end_time - start_time} seconds")
