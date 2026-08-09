Writing

🏥 Hospital Management System

A Python-based Hospital Management System built to practice Object-Oriented Programming and modular program design.

📌 About the Project

This project is a command-line Hospital Management System where the user can create a hospital and manage doctors, patients, and nurses using unique IDs. The project is organized into separate files for classes, menu handling, and hospital operations.

✅ Current Features

- Create a hospital with name and branch
- Add doctors, patients, and nurses
- Store people inside the hospital object
- Display individual doctors, patients, and nurses
- Display all doctors, patients, or nurses
- Search a person using their unique ID
- Remove a person using their unique ID
- Validate person IDs based on type:
  - Doctors → "2XXX"
  - Nurses → "3XXX"
  - Patients → "4XXX"
- Prevent duplicate IDs
- Validate name input
- Validate age input
- Validate gender input
- Handle empty lists gracefully
- Separate menu flow for Add, Search, Remove, and Display

🔄 Pending Feature

- Update a person’s details

🧱 Project Structure

- "main.py" — starts the program
- "menus.py" — handles the menu flow
- "hospital_functions.py" — handles creation, validation, search, remove, and display helpers
- "classes.py" — contains the OOP classes

🧠 OOP Concepts Used

- Classes and objects
- Inheritance
- Base and child classes
- "__init__"
- "self"
- Method overriding
- Lists of objects
- Object references
- Encapsulation of data through class methods

🆔 ID System

Each person has a unique ID:

- Doctor IDs: "2XXX"
- Nurse IDs: "3XXX"
- Patient IDs: "4XXX"

The program checks that:

- the ID contains only digits
- the ID has the correct length
- the ID belongs to the correct person type
- the ID is not already in use

🚀 How to Run

1. Make sure Python is installed.
2. Open the project folder.
3. Run:

python main.py

📘 Notes

This project is still under development. More features like update, better data management, and future persistence can be added later.