
# Student Transcript Management System

## Description
A comprehensive application designed to manage student transcripts effectively. The system provides functionalities such as creating, querying, modifying, deleting, and saving student information.

---

## Features

- **Menu-driven Interface**: Displays a welcome message with a user-friendly menu.
- **Modules**:
  - Create new student records.
  - Display all student records with sorting options.
  - Query specific student records with options to modify or delete.
- **Data Persistence**: Saves all information into a `student.csv` file upon exiting the system.

---
## Instructions
- When starting the program, display the welcome info along with the menu:
- The user can choose a module by pressing a relevant number;
- A module will be executed according to the user’s choice;
- The transcript is demanded to include the following information about a student: Major, ID, Name, Gender, Subject, Score;
- If a specific student is searched, the user can choose to modify or to delete this student’s information;
- The transcript will be saved when the system is quitted, and all info will be exported into a file called student.csv.
- Execution example of each module:


## Transcript Information
Each student's transcript includes:
- Major
- ID
- Name
- Gender
- Subject
- Score

---

## Modules and Execution

### 1. Welcome Info
```
****************************************
1. CREATE NEW
2. SHOW ALL
3. QUERY
0. SAVE AND QUIT
****************************************
```

### 2. CREATE NEW Module
**Execution Example**:
```
Create a new student: Please input the aspects of the student by turn:
Major: CST
ID: 2130130248
Name: MAHIM
Gender: Male
Subject: DSA
Score: 99
Student info successfully created.
Would you hope to continue to create a new one? Y/N
```

---

### 3. SHOW ALL Module
Displays all student records in a table format:
```
Major   ID  Name       Gender   Subject         Score
CST     01  Marco      Male     Intro-Com-Sci   85
CST     02  Alessandro Male     Intro-Com-Sci   95
CST     03  Matteo     Male     Intro-Com-Sci   85
CST     04  MAHIM      Male     Intro-Com-Sci   95
CST     05  Lucia      Female   Intro-Com-Sci   90
CST     06  Paola      Female   Intro-Com-Sci   95
```
**Sorting Options**:
1. Sort by ID
2. Sort by Score

**Direction**:
Use a data structure of your choice to store the data and implement at least two different sorting algorithms. Include time complexity evaluations in the report.

---

### 4. QUERY Module
**Execution Example**:
```
Please input the student name for query: MAHIM
Major   ID  Name       Gender   Subject         Score
CST     04  MAHIM      Male     Intro-Com-Sci   95
Please choose the operation on this student:
1. Modify
2. Delete
0. Back to the menu
```

#### Modify:
```
Input the new value for attribute "Major": SE
Input the new value for attribute "Subject": Python Coding
Input the new value for attribute "Score":  
Modification is successful!
Major   ID  Name       Gender   Subject         Score
SE      04  MAHIM      Male     Python Coding   95
```

#### Delete:
```
Entire row will be removed and the remaining students' info will be displayed.
```

---

### 5. Quit
Upon exiting, display:
```
File successfully saved. Welcome next use!
```

---

## File Output
All data is exported to `student.csv` using Python. Example format:
```
Major,ID,Name,Gender,Subject,Score
CST,01,Marco,Male,Intro-Com-Sci,85
CST,02,Alessandro,Male,Intro-Com-Sci,95
...
```

---

## Program Code
Include the code for each module in the repository.

---

## Learning Outcome
Summarize your key takeaways from building this system.
