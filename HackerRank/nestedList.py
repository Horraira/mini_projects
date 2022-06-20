# Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

# Example
# records = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

# The ordered list of scores is ... , so the second lowest score is . There are two students with that score: . Ordered alphabetically, the names are printed as: ...

students = int(input("Enter the amount of students: "))

records = []
for i in range(students):
    name = input("Enter the name of student: ")
    score = float(input("Enter the score of student: "))
    records.append([name,score]
    )

print(records)
# sort the records based on score


second_highest = sorted(list(set([b for a,b in records])))[1]

# array of students with second highest score
second_highest_students = [a for (a,b) in sorted(records) if b == second_highest]

print('\n'.join(second_highest_students))
