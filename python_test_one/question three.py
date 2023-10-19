#part i,
student_marks = [78, 83, 90, 88, 75]

# Calculate the sum of the items in the list
total_marks = sum(student_marks)

# Print the result
print(f"The sum of the items in the student marks list is {total_marks}.")

#part ii,
student_marks = [78, 83, 90, 88, 75]

# Display the first mark
first_mark = student_marks[0]
print("First mark:", first_mark)

# Display the last mark
last_mark = student_marks[-1]
print("Last mark:", last_mark)

#part iii
#add 96 to the list
# Existing list of student marks
student_marks = [78, 83, 90, 88, 75]

# Add 96 to the list
student_marks.append(96)

# Print the updated list
print(student_marks)


#part iv
# Existing list of student marks
student_marks = [78, 83, 90, 88, 75]

# Update the student mark from 78 to 87
index_to_update = student_marks.index(78)
student_marks[index_to_update] = 87

# Print the updated list
print(student_marks)
