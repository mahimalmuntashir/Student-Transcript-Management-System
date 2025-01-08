# MAHIM AL MUNTASHIR BILLAH
# 2130130248
# Algorithm Design and Analysis
# Curriculum Design for Data Structure and Algorithms

import csv

# Initialize the data list
data = []

# Load data from the CSV file
def load_data():
    try:
        with open("student.csv", "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                row['Score'] = int(row['Score'])  # Convert Score back to integer
                data.append(row)
    except FileNotFoundError:
        print("No previous data found. Starting with an empty dataset.")

# Function to display the menu
def display_menu():
    print("****************************************")
    print("1. CREATE NEW")
    print("2. SHOW ALL")
    print("3. QUERY")
    print("0. SAVE AND QUIT")
    print("****************************************")

# Function to create a new student
def create_new():
    while True:
        student = {
            "Major": input("Major: "),
            "ID": input("ID: "),
            "Name": input("Name: "),
            "Gender": input("Gender: "),
            "Subject": input("Subject: "),
            "Score": int(input("Score: ")),
        }
        data.append(student)
        print("Student info successfully created.")
        cont = input("Would you hope to continue to create a new one? (Y/N): ").strip().upper()
        if cont != 'Y':
            break

# Function to show all students
def show_all():
    if not data:
        print("No students found.")
        return
    print("Please choose the mode for display:")
    print("1. Sort by ID")
    print("2. Sort by Score")
    choice = int(input("Choice: "))

    if choice == 1:
        sorted_data = sorted(data, key=lambda x: x['ID'])
    elif choice == 2:
        sorted_data = sorted(data, key=lambda x: x['Score'], reverse=True)
    else:
        print("Invalid choice.")
        return

    print("+-------+------------+-----------------------+--------+----------------+-------+")
    print("| Major | ID         | Name                  | Gender | Subject        | Score |")
    print("+-------+------------+-----------------------+--------+----------------+-------+")
    for student in sorted_data:
        print(f"| {student['Major']:<5} | {student['ID']:<10} | {student['Name']:<21} | {student['Gender']:<6} | {student['Subject']:<14} | {student['Score']:<5} |")
    print("+-------+------------+-----------------------+--------+----------------+-------+")

# Function to query a student
def query():
    name = input("Please input the student name for query: ")
    found_students = [s for s in data if s['Name'].lower() == name.lower()]

    if not found_students:
        print("No student found with that name.")
        return

    print("+-------+------------+-----------------------+--------+----------------+-------+")
    print("| Major | ID         | Name                  | Gender | Subject        | Score |")
    print("+-------+------------+-----------------------+--------+----------------+-------+")
    for student in found_students:
        print(f"| {student['Major']:<5} | {student['ID']:<10} | {student['Name']:<21} | {student['Gender']:<6} | {student['Subject']:<14} | {student['Score']:<5} |")
    print("+-------+------------+-----------------------+--------+----------------+-------+")

    print("Please choose the operation on this student:")
    print("1. Modify")
    print("2. Delete")
    print("0. Back to the menu")
    choice = int(input("Choice: "))

    if choice == 1:
        modify(found_students[0])
    elif choice == 2:
        delete(found_students[0])

# Function to modify a student's details
def modify(student):
    student['Major'] = input(f"Input the new value for attribute 'Major' ({student['Major']}): ") or student['Major']
    student['Subject'] = input(f"Input the new value for attribute 'Subject' ({student['Subject']}): ") or student['Subject']
    try:
        student['Score'] = int(input(f"Input the new value for attribute 'Score' ({student['Score']}): ") or student['Score'])
    except ValueError:
        print("Invalid score, keeping the old value.")
    print("Modification is successful!")

    # Print the modified student details in table format
    print("+-------+------------+-----------------------+--------+----------------+-------+")
    print("| Major | ID         | Name                  | Gender | Subject        | Score |")
    print("+-------+------------+-----------------------+--------+----------------+-------+")
    print(f"| {student['Major']:<5} | {student['ID']:<10} | {student['Name']:<21} | {student['Gender']:<6} | {student['Subject']:<14} | {student['Score']:<5} |")
    print("+-------+------------+-----------------------+--------+----------------+-------+")

# Function to delete a student
def delete(student):
    data.remove(student)
    print("Student record deleted successfully.")

    # Display all remaining students in table format
    if data:
        print("+-------+------------+-----------------------+--------+----------------+-------+")
        print("| Major | ID         | Name                  | Gender | Subject        | Score |")
        print("+-------+------------+-----------------------+--------+----------------+-------+")
        for student in data:
            print(f"| {student['Major']:<5} | {student['ID']:<10} | {student['Name']:<21} | {student['Gender']:<6} | {student['Subject']:<14} | {student['Score']:<5} |")
        print("+-------+------------+-----------------------+--------+----------------+-------+")
    else:
        print("No students remain in the database.")

# Function to save data to a CSV file
def save_and_quit():
    with open("student.csv", "w", newline="") as csvfile:
        fieldnames = ["Major", "ID", "Name", "Gender", "Subject", "Score"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    print("File successfully saved. Welcome next use!")

# Main program
load_data()  # Load existing data from the CSV file
while True:
    display_menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        create_new()
    elif choice == 2:
        show_all()
    elif choice == 3:
        query()
    elif choice == 0:
        save_and_quit()
        break
    else:
        print("Invalid choice. Please try again.")
