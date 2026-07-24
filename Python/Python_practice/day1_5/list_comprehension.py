# List Comprehension = It is a consice way to create lists
# compact and easier way to create lists than traditional method
#   [expression for value in iterable if condition]

# doubles = [x * 2 for x in range(1,11)]

# print(doubles)

grades = [67,34,82,58,93,12]
passing_grades = [grade for grade in grades if grade >= 60]
print(passing_grades)