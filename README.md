# Neetcode
Neetcode problems and solutions
[Reference](https://www.w3schools.com/python/python_arrays.asp)

# Arrays
Python does not have built-in support for Arrays, but Python Lists can be used instead.

# Dictionary
Dictionary in Python is an unordered collection of data values, used to store data values like a map, which unlike other Data Types that hold only single value as an element, Dictionary holds key:value pair. Key-value is provided in the dictionary to make it more optimized. A regular dictionary type does not track the insertion order of the (key, value) pairs and thus iterates through the keys based on how they are stored in the hash table which in turn is based on random values so as to reduce collisions.
In contrast to this Python provides the OrderedDict type which remembers the insertion order of (key, value) pairs in the dictionary and thus preserves the order. OrderedDict consumes more memory than a regular dictionary in Python because of the underlying Doubly LinkedList implementation to preserving the order.

## Why is looking up entries in a dictionary so much faster?

Lookups are faster in dictionaries because Python implements them using hash tables.

If we explain the difference by Big O concepts, dictionaries have constant time complexity, O(1) while lists have linear time complexity, O(n).

[Reference](https://towardsdatascience.com/faster-lookups-in-python-1d7503e9cd38)
