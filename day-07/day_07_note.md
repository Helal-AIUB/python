1. What is file handling?

File handling is the process of creating, reading, writing, updating, and deleting files in a program.

2. Difference between read, write, and append mode
r (Read): Opens a file to read its contents. File must already exist.
w (Write): Opens a file for writing. Creates a new file or overwrites an existing one.
a (Append): Opens a file to add new data at the end without deleting existing data.
3. Why do we use with open()?

with open() automatically closes the file after use, even if an error occurs. It makes file handling safer and cleaner.

Example:

with open("file.txt", "r") as f:
    print(f.read())
4. What is exception handling?

Exception handling is a way to manage runtime errors so that the program does not crash.

Example:

try:
    print(10/0)
except ZeroDivisionError:
    print("Cannot divide by zero.")
5. Why do we use try-except?

We use try-except to catch and handle errors gracefully, preventing the program from stopping unexpectedly.

6. What is pip?

pip is Python's package manager. It is used to install, update, and remove Python libraries.

Example:

pip install requests
7. What is a virtual environment?

A virtual environment is an isolated Python environment where each project can have its own packages and dependencies.

Create one:

python -m venv venv
8. What is requirements.txt?

requirements.txt is a file that lists all the Python packages required for a project.

Example:

requests==2.32.0
numpy==2.0.0

Install all packages:

pip install -r requirements.txt
9. Which commands did you use today?

Some common commands are:

python filename.py
pip install package_name
python -m venv venv
venv\Scripts\activate
pip freeze > requirements.txt
pip install -r requirements.txt

10. What problems did you face during practice?
File not found (FileNotFoundError)
Wrong file mode (r, w, a)
Forgetting to activate the virtual environment
Missing Python packages
Syntax or indentation errors

11. What did you learn today?
Today I learned:
File handling in Python
Read, write, and append modes
Using with open()
Exception handling with try-except
Using pip to install packages
Creating a virtual environment
Managing project dependencies with requirements.txt