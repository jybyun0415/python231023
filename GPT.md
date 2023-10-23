# Lists
# - Pros: Ordered, mutable, allows duplicates, supports indexing and slicing.
# - Cons: Slower for membership testing and removing elements.

my_list = [1, 2, 3, 4, 5]
print("List:", my_list)

# Tuples
# - Pros: Ordered, immutable, faster than lists, can be used as keys in dictionaries.
# - Cons: Cannot be changed after creation.

my_tuple = (1, 2, 3, 4, 5)
print("Tuple:", my_tuple)

# Sets
# - Pros: Unordered, no duplicates, faster membership testing than lists/tuples.
# - Cons: Does not support indexing, elements are not stored in a specific order.

my_set = {1, 2, 3, 4, 5}
print("Set:", my_set)

# Dictionaries (Dicts)
# - Pros: Key-Value pairs for fast lookup, unordered but efficient for retrieval.
# - Cons: Keys must be unique, not ordered, slower than lists for iterating.

my_dict = {'a': 1, 'b': 2, 'c': 3}
print("Dictionary:", my_dict)
