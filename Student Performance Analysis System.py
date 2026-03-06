import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("students.csv")

print("\nStudent Dataset:\n")
print(data)

# Calculate class average
class_average = data["Marks"].mean()
print("\nClass Average Marks:", class_average)

# Top student
top_student = data.loc[data["Marks"].idxmax()]
print("\nTop Student:\n", top_student)

# Lowest student
low_student = data.loc[data["Marks"].idxmin()]
print("\nLowest Student:\n", low_student)

# Ranking students
data["Rank"] = data["Marks"].rank(ascending=False)

print("\nStudent Rankings:\n")
print(data)

# Bar chart of marks
plt.bar(data["Name"], data["Marks"])
plt.title("Student Performance")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# Pie chart
plt.figure()
plt.pie(data["Marks"], labels=data["Name"], autopct="%1.1f%%")
plt.title("Marks Distribution")
plt.show()
