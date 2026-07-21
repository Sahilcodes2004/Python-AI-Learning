import os

if not os.path.exists("data"):
    os.mkdir("data")

for i in range(0, 100):
    old_name = f"data/Day{i+1}"
    new_name = f"data/Tutorial{i+1}"
    
    # Check if destination ALREADY exists
    if os.path.exists(new_name):
        print(f"Skipped: '{new_name}' already exists.")
        continue # Skip to the next number
        
    # Check if the source folder actually exists before renaming
    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        print(f"Renamed: '{old_name}' -> '{new_name}'")
    else:
        print(f"Skipped: '{old_name}' not found.")