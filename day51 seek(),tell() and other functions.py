# Create a Python program that performs the following tasks:
# 1. Open a text file in the appropriate mode.
# 2. Write "Python is amazing" into the file.
# 3. Move the file pointer to position 7.
# 4. Display the current file pointer position.
# 5. Read the next 4 characters and display them.
# 6. Truncate the file so that only the first 6 characters remain.
# 7. Close the file.

f = open("day51 file.txt","r")
text = f.read()
print(text)
f.seek(7)
print(f.tell())
f.close()

