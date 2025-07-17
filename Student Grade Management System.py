import os

# File to store data
DATA_FILE = "grades.txt"

# Dictionary to store data in memory
students = {}

# Load data from file
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            for line in f:
                name, grade = line.strip().split(",")
                students[name] = grade

# Save data to file
def save_data():
    with open(DATA_FILE, "w") as f:
        for name, grade in students.items():
            f.write(f"{name},{grade}\n")

# Add student
def add_student():
    name = input("Enter student name: ").strip()
    if name in students:
        print("Student already exists.")
    else:
        grade = input("Enter grade: ").strip()
        students[name] = grade
        print(f"{name} added with grade {grade}.")

# View all students
def view_students():
    if not students:
        print("No student data available.")
    else:
        print("\n--- Student Grades ---")
        for name, grade in students.items():
            print(f"{name}: {grade}")
        print("----------------------")

# Search for student
def search_student():
    name = input("Enter student name to search: ").strip()
    if name in students:
        print(f"{name}'s grade: {students[name]}")
    else:
        print("Student not found.")

# Update student grade
def update_grade():
    name = input("Enter student name to update: ").strip()
    if name in students:
        grade = input("Enter new grade: ").strip()
        students[name] = grade
        print(f"{name}'s grade updated to {grade}.")
    else:
        print("Student not found.")

# Delete student
def delete_student():
    name = input("Enter student name to delete: ").strip()
    if name in students:
        del students[name]
        print(f"{name} deleted.")
    else:
        print("Student not found.")

# Main menu loop
def menu():
    load_data()
    while True:
        print("\n=== Student Grade Management ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Grade")
        print("5. Delete Student")
        print("6. Save & Exit")
        
        choice = input("Choose an option (1-6): ").strip()

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_grade()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            save_data()
            print("Data saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    menu()
