import os

print("Removing files from Downloads folder...")
path = r'D:\Users\Username\Downloads'

if not os.path.isdir(path):
    print("Directory not found")
    exit()

type_of_file = input("Enter types of files that you want to remove (separated by comma): ")
types = [x.strip() for x in type_of_file.split(",")]
new_lst = [file for file in os.listdir(path) if file.lower().endswith(tuple(types))]

count = len(new_lst)
for file in new_lst:
    try:
        os.remove(os.path.join(path, file))
    except Exception as e:
        print(f"Error deleting file {file}: {e}")

print(f"{count} files deleted.")
