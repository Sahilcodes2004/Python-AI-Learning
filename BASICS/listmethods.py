# ==========================================
# 🚀 PYTHON LIST METHODS REVISION SCRIPT
# ==========================================

# 1. CREATION & BASIC ACCESS
l = [2, 7, 1, 8, 3]
print("Original List l:", l)

# Accessing elements (0-indexed)
print("Element at index 2:", l[2]) 


# 2. ADDING ELEMENTS
# append() adds an element to the VERY END of the list. Fast operation O(1).
l.append(7)           

# insert(index, value) places an element at a specific position. 
# Everything else shifts right. Slower operation O(N).
l.insert(2, 100)      
print("After Append & Insert:", l)


# 3. SORTING & REVERSING (In-Place Modifications)
# sort() arranges elements in ascending order.
l.sort()              
print("Sorted (Ascending):", l)

# sort(reverse=True) arranges elements in descending order.
l.sort(reverse=True)  
print("Sorted (Descending):", l)

# reverse() flips the CURRENT order of the list (does not sort it).
l.reverse()           
print("Reversed:", l)


# 4. COUNTING & SEARCHING
# count(value) returns how many times a specific value appears in the list.
print("How many times does 4 appear?:", l.count(4)) 


# 5. COPYING LISTS (Crucial for DSA & Bug Prevention)
# copy() creates a BRAND NEW list in memory. 
# If you just did m = l, changing 'm' would accidentally change 'l' too!
m = l.copy()          
m[0] = 3              # Safe to modify 'm' without affecting 'l'
print("Copied and Modified List m:", m)


# 6. COMBINING LISTS
n = [90, 98, 989]

# extend() takes another list and adds all its elements to the end of the current list.
l.extend(m)           
print("List l after extending with m:", l)

# Concatenation (+) creates a completely NEW list 'k' without modifying 'l' or 'm'.
k = l + m             
print("Concatenated List k:", k)


# 🌟 BONUS: THE MISSING REMOVAL METHODS 🌟
# pop() removes and returns the LAST element. Used constantly in Stack problems!
l.pop()               

# remove(value) removes the FIRST occurrence of a specific value.
l.remove(100)         
print("After Pop and Remove:", l)