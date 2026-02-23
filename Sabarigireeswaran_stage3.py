# Stage 3: Student Grade Calculator

name = input("Enter student name: ")

mark1 = float(input("Enter marks for Subject 1 (0-100): "))
mark2 = float(input("Enter marks for Subject 2 (0-100): "))
mark3 = float(input("Enter marks for Subject 3 (0-100): "))

# Calculate total
total = mark1 + mark2 + mark3

# Calculate percentage
percentage = (total / 300) * 100

# Grade logic
if percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "F"

# Output
print("\nStudent Name:", name)
print("Total:", total, "/300")
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)