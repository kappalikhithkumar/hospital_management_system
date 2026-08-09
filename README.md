# 🏥 Hospital Management System
## Project Progress & TODO Checklist

---

## ✅ COMPLETED

### Project Structure
- [x] `main.py` — starts the program
- [x] `menus.py` — handles menus
- [x] `hospital_functions.py` — handles hospital/person operations
- [x] `classes.py` — contains OOP classes

### OOP
- [x] `Hospital` class
- [x] `Person` base class
- [x] `Doctor` class
- [x] `Patient` class
- [x] `Nurse` class
- [x] Inheritance
- [x] `super()`
- [x] Instance variables
- [x] Lists of objects
- [x] Hospital stores doctors, patients and nurses

### Hospital / Add Features
- [x] Create hospital
- [x] Add doctor
- [x] Add patient
- [x] Add nurse
- [x] Store doctors
- [x] Store patients
- [x] Store nurses

### Menus
- [x] Main menu
- [x] Add menu
- [x] Remove menu skeleton
- [x] Search menu skeleton
- [x] Display menu
- [x] Pass the same `hospital` object between menus

### Display
- [x] Display doctors
- [x] Display patients
- [x] Display nurses
- [x] Individual `display()` methods
- [x] Basic use of `super().display()`

---

# 🔴 CORE FEATURES PENDING

## 1. Search
- [ ] Search doctor
- [ ] Search patient
- [ ] Search nurse
- [ ] Handle person not found
- [ ] Handle empty lists
- [ ] Handle duplicate names
- [ ] Decide whether search is case-sensitive

## 2. Remove
- [ ] Remove doctor
- [ ] Remove patient
- [ ] Remove nurse
- [ ] Handle person not found
- [ ] Handle empty lists
- [ ] Decide how a person is identified for removal

## 3. Update
- [ ] Update doctor details
- [ ] Update patient details
- [ ] Update nurse details
- [ ] Decide which fields can be changed

---

# 🟠 INPUT VALIDATION

## Name
- [ ] Hospital name cannot be empty
- [ ] Branch cannot be empty
- [ ] Person name cannot be empty
- [ ] Reject/handle spaces-only input
- [ ] Decide whether numbers are allowed
- [ ] Decide whether special characters are allowed
- [ ] Decide how names are normalized
- [ ] Handle duplicate names

## Age
- [ ] Must be numeric
- [ ] Convert valid input to `int`
- [ ] Reject alphabetic input
- [ ] Reject special characters
- [ ] Reject negative age
- [ ] Decide whether `0` is allowed
- [ ] Decide reasonable maximum age
- [ ] Handle empty input

## Gender
- [ ] Accept only the chosen values (`M/F`, if that remains the design)
- [ ] Handle lowercase `m/f`
- [ ] Reject invalid values
- [ ] Handle empty input
- [ ] Decide whether `Male/Female` should also be accepted

## Doctor Specialization
- [ ] Cannot be empty
- [ ] Handle spaces-only input
- [ ] Decide allowed characters
- [ ] Decide whether duplicate specializations are allowed

## Nurse Shift
- [ ] Cannot be empty
- [ ] Decide allowed shifts
- [ ] Reject invalid shift
- [ ] Handle different capitalization

---

# 🟡 DUPLICATE / EDGE CASE HANDLING

- [ ] Decide whether duplicate person names are allowed
- [ ] If not allowed, prevent duplicate creation
- [ ] If allowed, make search/remove able to distinguish duplicates
- [ ] Consider introducing a unique ID later
- [ ] Handle empty hospital lists
- [ ] Handle search with no results
- [ ] Handle removal with no results
- [ ] Handle unexpected user input
- [ ] Prevent the program from crashing on invalid input

---

# 🔴 PERSON ID SYSTEM — IMPORTANT

Every person must have a **unique ID**.

## ID Series
- [X] Doctor IDs must use the `2XXX` series
- [X] Nurse IDs must use the `3XXX` series
- [X] Patient IDs must use the `4XXX` series

## ID Validation
- [X] Validate the ID format
- [X] Doctor ID must belong to `2XXX`
- [X] Nurse ID must belong to `3XXX`
- [X] Patient ID must belong to `4XXX`
- [X] Reject an ID from the wrong series
- [X] Reject duplicate IDs
- [X] Check whether the ID already exists before adding a person
- [ ] Handle invalid/non-existent IDs during search
- [ ] Handle invalid/non-existent IDs during removal
- [ ] Handle invalid/non-existent IDs during update
- [ ] Decide the exact valid range within each series
- [X] Decide whether IDs are stored as integers or strings

## ID-Based Operations
- [ ] Search a person using their unique ID
- [ ] Remove a person using their unique ID
- [ ] Update a person using their unique ID
- [ ] Display the person's ID with their details
- [ ] Keep IDs unique across the hospital

## ID Design Decision
- [ ] Decide whether IDs are manually entered or automatically generated
- [X] If manually entered, validate every ID
- [ ] If automatically generated later, generate the next available ID in the correct series

---

# 🟡 MENU VALIDATION

- [ ] Invalid main-menu choice
- [ ] Invalid add-menu choice
- [ ] Invalid remove-menu choice
- [ ] Invalid search-menu choice
- [ ] Invalid display-menu choice
- [ ] Show a clear error message
- [ ] Return to the correct menu after invalid input
- [ ] Use `Back` instead of `Exit` for submenus where appropriate

---

# 🟡 DISPLAY IMPROVEMENTS

- [ ] Show a message when no doctors exist
- [ ] Show a message when no patients exist
- [ ] Show a message when no nurses exist
- [ ] Fix Nurse display label: `Shift`, not `Specialization`
- [ ] Fix Patient display label: `Age`, not `Specialization`
- [ ] Improve display formatting if needed

---

# 🧹 CODE QUALITY

- [ ] Remove unnecessary imports
- [ ] Keep each file responsible for one area
- [ ] Avoid duplicate code
- [ ] Use meaningful function names
- [ ] Keep menus separate from hospital operations
- [ ] Keep classes separate from UI code
- [ ] Add comments/docstrings where useful
- [ ] Test after each major feature

---

# 🧪 TESTING CHECKLIST

For every feature, test:

- [ ] Normal/correct input
- [ ] Wrong input
- [ ] Empty input
- [ ] Duplicate input
- [ ] Not-found case
- [ ] Empty list
- [ ] Boundary values
- [ ] Unexpected user behavior
- [ ] Repeated operations
- [ ] Returning between menus
- [ ] Exiting the program

---

# 📋 CURRENT FUNCTION STATUS

## `classes.py`

### Hospital
- [x] `__init__`
- [x] `add_doctor()`
- [x] `add_patient()`
- [x] `add_nurse()`
- [x] `display_doctors()`
- [x] `display_patients()`
- [x] `display_nurses()`
- [ ] `remove_doctor()`
- [ ] `remove_patient()`
- [ ] `remove_nurse()`
- [ ] Search methods if needed
- [ ] Update methods if needed

### Person
- [x] `__init__`
- [x] `display()`

### Doctor
- [x] `__init__`
- [ ] Add unique ID
- [x] `display()`

### Patient
- [x] `__init__`
- [ ] Add unique ID
- [x] `display()`

### Nurse
- [x] `__init__`
- [ ] Add unique ID
- [x] `display()`

---

## `hospital_functions.py`

### Create
- [x] `create_hospital()`
- [x] `create_doctor()`
- [x] `create_patient()`
- [x] `create_nurse()`

### Display
- [x] `display_doctor()`
- [x] `display_patient()`
- [x] `display_nurse()`

### Search
- [ ] `search_doctor()`
- [ ] `search_patient()`
- [ ] `search_nurse()`

### Remove
- [ ] `remove_doctor()`
- [ ] `remove_patient()`
- [ ] `remove_nurse()`

### Update
- [ ] `update_doctor()`
- [ ] `update_patient()`
- [ ] `update_nurse()`

---

## `menus.py`

- [x] `main_menu()`
- [x] `add_menu()`
- [x] `remove_menu()` skeleton
- [x] `search_menu()` skeleton
- [x] `display_menu()`

### Connect pending features
- [ ] Connect search functions
- [ ] Connect remove functions
- [ ] Connect update functions when added
- [ ] Validate submenu choices

---

## `main.py`

- [x] Start program
- [x] Create hospital
- [x] Pass hospital to `main_menu()`
- [ ] Remove unnecessary imports
- [ ] Keep `main.py` minimal

---

# 🗓️ NEXT WORK SESSION

## Priority 1 — Fix tiny existing issues
- [ ] Fix Nurse display text
- [ ] Fix Patient display text
- [ ] Clean unnecessary imports

## Priority 2 — Person ID System
- [ ] Add ID to person data
- [ ] Decide ID input/generation method
- [ ] Validate Doctor `2XX`
- [ ] Validate Nurse `3XX`
- [ ] Validate Patient `4XX`
- [ ] Prevent duplicate IDs
- [ ] Test wrong-series IDs
- [ ] Test duplicate IDs

## Priority 3 — Search
- [ ] Search by unique ID
- [ ] Design search logic
- [ ] Implement doctor search
- [ ] Implement patient search
- [ ] Implement nurse search
- [ ] Test search

## Priority 4 — Remove
- [ ] Design removal logic
- [ ] Implement doctor removal
- [ ] Implement patient removal
- [ ] Implement nurse removal
- [ ] Test removal

## Priority 5 — Input validation
- [ ] Name
- [ ] Age
- [ ] Gender
- [ ] Specialization
- [ ] Nurse shift
- [ ] Empty input
- [ ] Invalid input
- [ ] Duplicate input

---

# 🚀 FUTURE FEATURES

These are ideas for later — NOT current tasks.

- [ ] Unique IDs for people
- [ ] Doctor ↔ patient relationships
- [ ] Appointments
- [ ] Doctor availability
- [ ] Nurse assignments
- [ ] Patient medical information
- [ ] Hospital statistics
- [ ] Save data to file
- [ ] Load data when program starts
- [ ] SQLite database
- [ ] Login/admin system
- [ ] GUI
- [ ] Convert project to `.exe`

---

# 🧠 OOP LEARNING TRACK

### Already covered
- [x] Classes and objects
- [x] `__init__`
- [x] `self`
- [x] Instance variables
- [x] Lists of objects
- [x] Object references
- [x] Methods
- [x] Inheritance
- [x] `super()`
- [x] Method overriding

### Later
- [ ] Object searching
- [ ] Object removal
- [ ] Object updating
- [ ] Encapsulation
- [ ] Properties
- [ ] Polymorphism
- [ ] More advanced OOP design

---

## ⭐ PROJECT RULE

Do not mark a feature as complete just because the normal case works.

A feature is complete only after it handles:

**Correct input + invalid input + empty input + duplicate input + wrong ID series + duplicate ID + not-found cases + edge cases + menu flow.**
