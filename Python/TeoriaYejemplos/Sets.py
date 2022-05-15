"""
SETS are used to store multiple items in a single variable.
    - Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are LIST, TUPLE, and DICTIONARY, all with different qualities and usage.
    - A set is a collection which is unordered, unchangeable*, unindexed and DO NOT allow DUPLICATE values.
    - Sets are written with curly brackets.
    - Set can contain ANY DATA TYPE

* Note: Set items are UNCHANGEABLE: Once a set is created, you cannot change its items but you can REMOVE items and ADD new items.
* Note: Sets are unordered, so you cannot be sure in which order the items will appear, cannot be referred to by index or key.

--> Example: Create a Set

thisset = {"abc", 34, True, 40, "male"}
print(thisset)
"""
#========|| Access Items ||========================
#You cannot access items in a set by referring to an index or a key.
#But you can loop through the set items using a for loop, ORRR ask if a specified value is present in a set, by using the in keyword.

#Example: Loop through the set, and print the values:
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

#Example: Check if "banana" is present in the set:
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset) # -> True

#========|| Add Items ||========================
#Once a set is created, you cannot change its items, but you can add new items.
#To add one item to a set use the add() method.

#Example: Add an item to a set, using the add() method:
thisset = {"apple", "banana", "cherry"}
print(thisset)
thisset.add("orange")
print(thisset)

#========|| Add Sets ||========================
# To add items from another set into the current set, use the update() method.

#Example: Add elements from tropical into thisset:
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
print(thisset)              # -> {'apple', 'banana', 'cherry'}
thisset.update(tropical)    # -> {'mango', 'papaya', 'cherry', 'pineapple', 'apple', 'banana'}
print(thisset)

#========|| Add Any Iterable ||====================
#The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

#Example: Add elements of a LIST to at SET:
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)  # -> {'kiwi', 'orange', 'apple', 'cherry', 'banana'}
                        # NOTE: que devuelve un SET y los items de la lista aparecen al principio (¿o en cualquier lugar????)
print(thisset)

#========|| Remove Item: .remove(),  .discard()  and   pop() ||========================
#To remove an item in a set, use the .remove(), or the .discard() method.
#       -NOTE: If the item to remove does not exist, .remove() will raise an ERROR.
#       -NOTE: If the item to remove does not exist, .discard() will NOT raise an ERROR.

#-------|| .remove() ||-------
#Example: Remove "banana" by using the remove() method:
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")    # -> {'cherry', 'apple'}
                            #NOTE: no queda ordenado!!!!
print(thisset)

#-------|| .discard() ||---------
#Example: Remove "banana" by using the discard() method:
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")   # -> {'apple', 'cherry'}
                            #NOTE: Parece que queda ordenado!!!!
print(thisset)

#------|| .pop() ||--------------
#NOTE: You can also use the .pop() method to remove an item, but this method will remove the last item. Remember that sets are unordered, so you will NOT KNOW what item that gets removed.

#Example: Remove the last item by using the .pop() method:
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()   # -> cherry
print(x)
print(thisset)      # -> {'banana', 'apple'}

#========|| Empty Set: .clear()  and  del ||========================

#------|| .clear() ||--------------
#Example: The .clear() method empties the set:
thisset = {"apple", "banana", "cherry"}
thisset.clear() # --> set()  vacío
print(thisset)

#------|| del ||--------------
#Example: The del keyword will delete the set COMPLETELY:
thisset = {"apple", "banana", "cherry"}
print(thisset)
del thisset     # -> NameError: name 'thisset' is not defined
                # ¡Ya no existe!
print(thisset)

#========|| SET METHODS ||========================
"""
METHOD	DESCRIPTION
add()	            Adds an element to the set
clear()	            Removes all the elements from the set
copy()	            Returns a copy of the set
difference()        Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
discard()	        Remove the specified item
intersection()	    Returns a set, that is the intersection of two other sets
intersection_update() Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	    Returns whether two sets have a intersection or not
issubset()	        Returns whether another set contains this set or not
issuperset()	    Returns whether this set contains another set or not
pop()	            Removes an element from the set
remove()	        Removes the specified element
symmetric_difference() Returns a set with the symmetric differences of two sets
symmetric_difference_update() Inserts the symmetric differences from this set and another
union()	            Return a set containing the union of sets
update()	        Update the set with the union of this set and others
"""
