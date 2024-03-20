from collections import Counter
a = "habtamuuuuuuuufeeyraaaaaaaa"
my_counter = Counter(a)
print(my_counter)

print("this is new print files")
print(my_counter.items())
#
print(my_counter.keys())
print(my_counter.values())


my_list = [0, 1, 0, 1, 2, 1, 1, 3, 2, 3, 2, 4]
my_counter = Counter(my_list)
print(my_counter)

# most common items
#print(my_counter.most_common(1))

# Return an iterator over elements repeating each as many times as its count. 
# Elements are returned in arbitrary order.
#print(list(my_counter.elements()))