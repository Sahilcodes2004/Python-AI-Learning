'''char = input("Enter a single letter: ").lower()

match char:
    case 'a' | 'e' | 'i' | 'o' | 'u':
        print(f"'{char}' is a Vowel.")
    case _ if char.isalpha(): # Guard clause ensures it's actually a letter
        print(f"'{char}' is a Consonant.")
    case _:
        print("Invalid input! Please enter an alphabet letter.")'''
x = int(input("Enter your marks: "))

match x:
    # 1. Catch invalid numbers first (The Bouncers)
    case _ if x < 0 or x > 100:
        print("Wrong input! Please enter a valid score between 0 and 100.")
        
    # 2. Now we know the number is safely between 0 and 100
    case _ if x >= 90:
        print("Grade A, Excellent work")
        
    case _ if x >= 80:
        print("Grade B, Good work")
        
    case _ if x >= 70:
        print("Grade C, Nice performance")
        
    case _ if x >= 0:
        print("Grade D, You need to work hard")