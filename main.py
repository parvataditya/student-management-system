#Write a Python program to create a text file containing student details

import os
import csv

FILENAME = "students.csv"
HEADERS = ["Roll Number", "Name", "Course", "Marks"]


def initialize_file():
    """Create the file with headers if it doesn't exist."""
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(HEADERS)


def add_record():
    """Append a new student record to the CSV file."""
    roll = input("Enter Roll Number: ").strip()
    name = input("Enter Name: ").strip()
    course = input("Enter Course: ").strip()

    while True:
        marks = input("Enter Marks: ").strip()
        if marks.replace(".", "", 1).isdigit():
            break
        print("Invalid marks. Please enter a number.")

    with open(FILENAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([roll, name, course, marks])

    print("Record added successfully.\n")


def display_records():
    """Display all student records in a formatted table."""
    if not os.path.exists(FILENAME) or os.path.getsize(FILENAME) == 0:
        print("No records found.\n")
        return

    with open(FILENAME, "r", newline="") as f:
        reader = csv.reader(f)
        rows = list(reader)

    if len(rows) <= 1:
        print("No records found.\n")
        return

    print(f"\n{'Roll No':<10}{'Name':<15}{'Course':<15}{'Marks':<10}")
    print("-" * 50)
    for row in rows[1:]:  # skip header
        roll, name, course, marks = row
        print(f"{roll:<10}{name:<15}{course:<15}{marks:<10}")
    print()


def search_record():
    """Search for a student by Roll Number."""
    if not os.path.exists(FILENAME):
        print("No records found.\n")
        return

    roll_to_find = input("Enter Roll Number to search: ").strip()

    with open(FILENAME, "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Roll Number"] == roll_to_find:
                print(f"\nRecord found:")
                print(f"Roll Number: {row['Roll Number']}")
                print(f"Name: {row['Name']}")
                print(f"Course: {row['Course']}")
                print(f"Marks: {row['Marks']}\n")
                return

    print("Record not found.\n")


def update_marks():
    """Update a student's marks by Roll Number."""
    if not os.path.exists(FILENAME):
        print("No records found.\n")
        return

    roll_to_update = input("Enter Roll Number to update: ").strip()

    with open(FILENAME, "r", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = reader.fieldnames

    updated = False
    for row in rows:
        if row["Roll Number"] == roll_to_update:
            while True:
                new_marks = input(f"Enter new marks for {row['Name']}: ").strip()
                if new_marks.replace(".", "", 1).isdigit():
                    break
                print("Invalid marks. Please enter a number.")
            row["Marks"] = new_marks
            updated = True
            break

    if updated:
        with open(FILENAME, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        print("Marks updated successfully.\n")
    else:
        print("Record not found.\n")


def main():
    initialize_file()

    while True:
        print("===== Student Record Management =====")
        print("1. Add New Record")
        print("2. Display All Records")
        print("3. Search by Roll Number")
        print("4. Update Marks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_record()
        elif choice == "2":
            display_records()
        elif choice == "3":
            search_record()
        elif choice == "4":
            update_marks()
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
