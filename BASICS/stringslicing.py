
"""
PYTHON STRINGS REVISION CHEAT SHEET
-----------------------------------
GOLDEN RULE: Strings in Python are IMMUTABLE. 
Whenever you use a method like .upper() or .replace(), Python DOES NOT change the 
original string. It creates and returns a brand new modified copy.
"""

# ==========================================
# 1. STRING SLICING [start : end]
# ==========================================
names = "sahil,mary"

# Prints characters from index 0 up to (but not including) 5 -> "sahil"
print("0 to 5:", names[0:5]) 

# len() gives the total number of characters -> 10
print("Length:", len(names)) 

# Negative slicing: starts 5 from the end, stops 2 from the end -> ",ma"
print("Negative Slicing:", names[-5:-2]) 

# Leaves start/end blank, meaning "print the whole string" -> "sahil,mary"
print("Full Slice:", names[:]) 

# Starts at index 3 and goes to the very end -> "il,mary"
print("Start at 3:", names[3:]) 


# ==========================================
# 2. CHANGING CASING & CLEANING STRINGS
# ==========================================
name2 = "AlEx BEnjaMin@@@"
language = "pythoN"

# Converts everything to lowercase -> "alex benjamin@@@"
print("Lower:", name2.lower())

# Converts everything to uppercase -> "ALEX BENJAMIN@@@"
print("Upper:", name2.upper())

# rstrip() removes the specific trailing character at the right end -> "AlEx BEnjaMin"
print("Strip @:", name2.rstrip("@"))

# Replaces a specific word/character with a new one -> "John BEnjaMin@@@"
print("Replace:", name2.replace("AlEx", "John"))

# Makes ONLY the very first letter uppercase, everything else lower -> "Python"
print("Capitalize:", language.capitalize())

# Swaps lower to upper, and upper to lower -> "aLeX beNJAmIN@@@"
print("Swapcase:", name2.swapcase())


# ==========================================
# 3. SEARCHING & FORMATTING
# ==========================================
intro = "Welcome to python string tutorial"

# Adds spaces around the string to center it within a 100-character width
print("Center:", intro.center(100))

# Counts how many times "to" appears in the string -> 2
print("Count 'to':", intro.count("to"))

# Finds the first index where "to" starts. Returns -1 if not found -> 8
print("Find 'to':", intro.find("to"))

# Returns True if the string starts with "Wel" -> True
print("Starts with Wel:", intro.startswith("Wel"))

# Returns True if the string ends with "!" -> False
print("Ends with !:", intro.endswith("!"))


# ==========================================
# 4. BOOLEAN (TRUE/FALSE) VALIDATION CHECKS
# ==========================================
str3 = "hello"

# isalnum() -> True if string has ONLY letters (A-Z) and numbers (0-9). No spaces!
print("Is Alphanumeric?:", names.isalnum()) # False because of the comma ','

# isalpha() -> True if string has ONLY letters (no numbers, no spaces)
print("Is Alphabetic?:", str3.isalpha()) # True for "hello"

# islower() -> True if all letters in the string are lowercase
print("Is Lowercase?:", str3.islower()) 

# isupper() -> True if all letters in the string are uppercase
print("Is Uppercase?:", str3.isupper()) 

# istitle() -> True if the first letter of EVERY word is capitalized (Like a Book Title)
print("Is Title?:", intro.istitle()) # False for "Welcome to python..."

# isspace() -> True if the string contains ONLY blank spaces ("   ")
print("Is Space?:", "   ".isspace()) 

# isprintable() -> True if everything can be printed (False if it has hidden characters like \n for new line)
print("Is Printable?:", intro.isprintable())
