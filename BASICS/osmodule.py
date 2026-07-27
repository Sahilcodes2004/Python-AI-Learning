import os
current_dir=os.getcwd();
print(f"1.In {current_dir}")


folder_name="Revision data"
folderpath=os.path.join(current_dir,folder_name)

if(not os.path.exists(folderpath)):
    os.mkdir(folderpath)
print(os.getcwd())


os.chdir(folderpath)
print(f"3.Moved into {os.getcwd()} ")

file="test_file.txt"
with open( file,"w") as f:
    f.write("Learning the os module ")
print(f"Created a file named {file}")

new_file="renamed.txt"
os.rename(file,new_file)
print(f"renamed the {file} to {new_file}")


os.remove(new_file)
print("Deleted the file")

os.chdir(current_dir)
os.rmdir(folderpath)
print("deletd the folder")



    
