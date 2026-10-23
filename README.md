# Student Record Management System

A simple Python-based Student Record Management System that stores student details in a CSV file. It allows users to add, display, search, and update student records through a menu-driven interface.

## Features

- **Add Student Record:** Enter roll number, name, course, and marks.
- **Display All Records:** View all student records in a formatted table.
- **Search Student:** Find a student using their roll number.
- **Update Marks:** Modify the marks of an existing student.
- **Input Validation:** Checks that marks are entered as a number.
- **CSV File Storage:** Saves student data permanently in `students.csv`.
- **Automatic File Creation:** Creates the CSV file with column headers if it does not exist.

## Technologies Used

- Python 3
- CSV Module
- OS Module

## Project Structure

```text
Student-Record-Management/
│
├── main.py
├── students.csv
├── README.md
└── .gitignore
```

*Note: Replace `main.py` with your actual Python filename if it is different. The `students.csv` file is created automatically when the program runs.*

## Requirements

- Python 3.x
- No external libraries required.

## How to Run

1. Clone or download this repository.
2. Open the project folder in VS Code or a terminal.
3. Run the following command:

```bash
python main.py
```

If your system uses `python3`, run:

```bash
python3 main.py
```

## Menu Options

```text
===== Student Record Management =====
1. Add New Record
2. Display All Records
3. Search by Roll Number
4. Update Marks
5. Exit
```

Choose an option from 1 to 5 and follow the instructions displayed on the screen.

## Data Storage

Student details are stored in `students.csv` with the following columns:

- Roll Number
- Name
- Course
- Marks

## Learning Outcomes

- Understanding file handling in Python.
- Working with CSV files using the `csv` module.
- Using functions and loops to organize a program.
- Implementing searching and updating operations.
- Applying input validation and menu-driven programming.

## Author

Aditya Kumar

## License

This project is available for educational and learning purposes.
