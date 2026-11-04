t = (10, 20, 30, 40, 20, 50)

print(t.index(20, 2, 6)) # start finding 20 from index 2 till 6-1(excluding index 6)

# Create a Tuple containing the marks of a student in 7 subjects. Some marks should be repeated.
# Print the original Tuple.
# Ask the user to enter a mark and display how many times it occurs.
# Ask the user to enter a mark and display its first index.
# Handle the situation when the entered mark is not present in the Tuple.
# Ask the user whether they want to modify the marks.
# If yes:
# - Convert the Tuple into a List.
# - Append a new mark.
# - Remove one existing mark .
# - Convert the List back into a Tuple.
# Create another Tuple containing marks of another student.
# Concatenate both Tuples into a new Tuple.
# Display the final Tuple and its total number of elements.

marks=(32,61,94,34,85,25,46)
print(marks)

x= int(input("Whose occurance you want to know: "))
print(marks.count(x))

i=int(input("Whose index you want to know: "))
if i in marks:
    print(marks.index(i))
else:
    print(i,"is not available")

edit = input("Do you want to modify marks?(y/n): ")
if edit == "y":
    temp = list(marks)
    print("list:",temp)
    add = int(input("Enter the mark(s) you want to add: "))
    temp.append(add)
    cut = int(input("Enter the mark(s) you want to remove: "))
    temp.remove(cut)
    marks = tuple(temp)
    print("marks/tuple:",marks,type(marks))

marks2 = (32,65,94,65,78,25)
print("marks of another student:",marks2)

both_marks = marks+marks2
print("concatinated",both_marks)
print("Length:",len(both_marks))