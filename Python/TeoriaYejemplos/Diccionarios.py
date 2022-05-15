"""
DICTIONARY: Dictionaries are used to store data values in: key: value pairs.
    A dictionary is a collection which is:
        -ORDERED: As of Python version 3.7, dictionaries are ordered (It means that the items have a defined order, and that order will not change.). In Python 3.6 and earlier, dictionaries are unordered (means that the items does not have a defined order, you CANNOT refer to an item by using an index.)
        -Changeable: we can change, add or remove items.
        -Do not allow duplicates: cannot have two items with the same key.
    --> Example:
dict_example = {
  "key1": "value1",
  "model": "value2",
  "year": 1964
}"""
"""
INDEX:
* Dictionary Items
* Accessing Items (basic method, .get(), .keys(), .values() y actualización de valores)
* Adding new Item
* Ordered or Unordered?
* Dictionary Methods
"""
#=====|| Dictionary Items ||======================
#Dictionary items are ORDERED, changeable, and does not allow duplicates.
#Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
#-->Example

#Print the "brand" value of the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"]) # returns 'Ford'
print(len(thisdict)) # returns how many items the dictionary has (here: 3 items)

#========|| Accessing Items ||========================
#You can access the items of a dictionary by referring to its key name, inside square brackets:
# --> Example

#Get the value of the "model" key:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"] # returns 'Mustang'
print(x)

#------|| .get() ||----------------
# There is also a method called get() that will give you the SAME RESULT:
# --> Example

#Get the value of the "model" key:
x = thisdict.get("model") # returns 'Mustang', SAME RESULT
print(x)

#------|| .keys() ||------------------
#The keys() method will return a LIST (¡Sí, una LISTA!) OF ALL THE KEYS in the dictionary.
# --> Example

#Get a list of the keys:
x = thisdict.keys() # returns dict_keys(['brand', 'model', 'year'])
print(x)

#------|| .values() y actualización de valores ||------------------
#Make a change in the original dictionary, and see that the values list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()

print(x) #before the change

car["year"] = 2020  # Actualizamos el valor para la clave "year"

print(x) #after the change

#------|| Adding new item ||------------------
#Add a new item to the original dictionary, and see that the keys list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys() #returns -> dict_keys(['brand', 'model', 'year'])

print(x) #before the change

car["color"] = "white"  # Crea un key 'color' de valor 'white' ||   "color": "white",
                        # returns -> dict_keys(['brand', 'model', 'year', 'color'])

print(x) #after the change

#=======|| Ordered or Unordered? ||==============
"""
As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

When we say that dictionaries are ORDERED, it means that the items have a defined order, and that order will not change.

Unordered means that the items does not have a defined order, you CANNOT refer to an item by using an index.
"""

#=========|| Dictionary Methods ||=====================
"""
METHOD	    DESCRIPTION
clear()	    Removes all the elements from the dictionary
copy()	    Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	    Returns the value of the specified key
items()	    Returns a list containing a tuple for each key value pair
keys()	    Returns a list containing the dictionary's keys
pop()	    Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()Returns the value of the specified key. 
            If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary      """

"""
Python Collections (Arrays)
There are four collection data types in the Python programming language:

* List is a collection which is ordered and changeable. Allows duplicate members.
* Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
* Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
* Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""