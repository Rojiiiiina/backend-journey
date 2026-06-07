
# #python list methods(append, insert, remove, pop, clear, index, count, sort, reverse)
# # append()method is used to add an element at the end of the list. It takes a single arguement which is the element to be added.
# cities = ["Jhapa", "Morang", "Sunsari", "Dhankuta", "Ilam"]

# cities.append("Taplejung")
# print(cities)

# # # insert() method is used to add an element at a specific position in the list. It takes two arguments, the first is the index when the element is to be added and the second is the element itself.
# cities.insert(2, "Khotang")
# print(cities)
# # # remove() method is used to remove the first occurence of an element from the list. It takes a single argument which is the element to be removed. If the element is not found in the list, it raises a ValueError.
# cities.remove("Sunsari")
# print(cities)
# # # pop() method is used to remove an element from the list at a specific index. It takes a single argument which is the index of the element to be removed. If the index is not present in the list it raises an IndexError. If no index is specified, it removes the last element from the list.
# cities.pop(3)
# print(cities)
# # # clear() method is used to remove all the elements from the list. It does not take any arguments.
# cities.clear()
# print(cities)  
# # # index() method is used to find the index of the first occurrence of an element in the list. It takes a single argument which is the element to be searched. If the element is not found in the list, it raises a ValueError.
# cities = ["Jhapa","Jhapa", "Morang", "Sunsari", "Dhankuta", "Ilam"]
# print(cities.index("Dhankuta"))
# # # count() method is used to count the number of occurrences of an element in the list. It takes a single argument which is the element to be counted.
# print(cities.count("Jhapa"))
# # # sort() method is used to sort the elements of the list in ascending order. It does not take any arguments.
# cities.sort()
# print(cities)
# # # reverse() method is used to reverse the order of the elements in the list. It does not take any arguments.
# cities.reverse()
# print(cities)
# # # copy() method is used to create a copy of the list. It does not take any arguments.
# cities_copy = cities.copy()
# print(cities_copy)
# # # extend() method is used to add the elements of another list to the end of the current list. It takes a single argument which is the list whose elements are to be added.
# more_cities = ["Khotang", "Taplejung"]
# cities.extend(more_cities)
# print(cities)

# # Python dictionary methods (clear, copy, fromkeys, get, items, keys, pop, popitem, setdefault, update, values)
# # clear() method is used to remove all the elements from the dictionary. It does not take any arguments.
# cities_population = {"Jhapa": 800000, "Morang": 900000, "Sunsari": 700000, "Dhankuta": 500000, "Ilam": 600000}
# cities_population.clear()
# print(cities_population)
# # copy() method is used to create a copy of the dictionary. It does not take any arguments.
# cities_population_copy = cities_population.copy()
# print(cities_population_copy)
# # fromkeys() method is used to create a new dictionary with the specified keys and values. It takes two arguments, the first is a list of keys and the second is the value to be assigned to all the keys.
# keys = ["Jhapa", "Morang", "Sunsari", "Dhankuta", "Ilam"]
# value = 10   
# new_dict = dict.fromkeys(keys, value)
# print(new_dict)
# # get() method is used to get the value of a specific key in the dictionary. It takes a single argument which is the key whose value is to be retrieved. If the key is not found in the dictionary, it returns None.
# print(cities_population.get("Jhapa"))
# # items() method is used to get a list of all the key-value pairs in the dictionary. It does not take any arguments.
# print(cities_population.items())
# # keys() method is used to get a list of all the keys in the dictionary. It does not take any arguments.
# print(new_dict.keys())
# # values() method is used to get a list of all the values in the dictionary. It does not take any arguments.
# print(new_dict.values())
# # pop() method is used to remove a specific key-value pair from the dictionary. It takes a single argument which is the key of the key-value pair to be removed. If the key is not found in the dictionary, it raises a KeyError.
# new_dict.pop("Jhapa")
# print(new_dict)
# # popitem() method is used to remove the last key-value pair from the dictionary. It does not take any arguments. If the dictionary is empty, it raises a KeyError.
# new_dict.popitem()  
# print(new_dict)
# # setdefault() method is used to get the value of a specific key in the dictionary. If the key is not found in the dictionary, it adds the key with the specified value and returns the value. It takes two arguments, the first is the key to be searched and the second is the value to be assigned if the key is not found.
# print(new_dict.setdefault("Khotang", 20))   
# # update() method is used to update the dictionary with the key-value pairs from another dictionary. It takes a single argument which is the dictionary whose key-value pairs are to be added to the current dictionary.
# another_dict = {"Taplejung": 30, "Panchthar": 40}
# new_dict.update(another_dict)   
# print(new_dict)
# # Tuples
# # count() method is used to count the number of occurrences of an element in the tuple. It takes a single argument which is the element to be counted.
# my_tuple = (1, 2, 3, 4, 5, 1, 2, 3)
# print(my_tuple.count(1))
# # index() method is used to find the index of the first occurrence of an element in the tuple. It takes a single argument which is the element to be searched. If the element is not found in the tuple, it raises a ValueError.
# print(my_tuple.index(3))    
