# Define two sample sets
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

# Print the sets
print("Set 1:", set1)
print("Set 2:", set2)

# Union of sets
print("\nUnion of Set 1 and Set 2:", set1 | set2)  # Using | operator
print("Union of Set 1 and Set 2 (method):", set1.union(set2))  # Using union() method

# Intersection of sets
print("\nIntersection of Set 1 and Set 2:", set1 & set2)  # Using & operator
print("Intersection of Set 1 and Set 2 (method):", set1.intersection(set2))  # Using intersection() method

# Difference of sets
print("\nDifference of Set 1 and Set 2:", set1 - set2)  # Using - operator
print("Difference of Set 1 and Set 2 (method):", set1.difference(set2))  # Using difference() method

# Symmetric difference of sets
print("\nSymmetric Difference of Set 1 and Set 2:", set1 ^ set2)  # Using ^ operator
print("Symmetric Difference of Set 1 and Set 2 (method):", set1.symmetric_difference(set2))  # Using symmetric_difference() method

# Checking subsets
subset = {3, 4}
print("\nIs", subset, "a subset of Set 1?", subset.issubset(set1))  # Using issubset() method
print("Is Set 1 a subset of", set2, "?", set1.issubset(set2))  # Using issubset() method

# Checking supersets
superset = {1, 2, 3, 4, 5, 6, 7}
print("\nIs Set 1 a superset of", superset, "?", set1.issuperset(superset))  # Using issuperset() method
print("Is", set2, "a superset of Set 1?", set2.issuperset(set1))  # Using issuperset() method
