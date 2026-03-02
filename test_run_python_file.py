from functions.run_python_file import run_python_file

# 1. Basic execution (No arguments)
print('run_python_file("calculator", "main.py"):')
print("Result:")
print("  " + run_python_file("calculator", "main.py").replace("\n", "\n  "))
print("-" * 30)

# 2. Execution with arguments (Calculation)
print('run_python_file("calculator", "main.py", ["3 + 5"]):')
print("Result:")
print("  " + run_python_file("calculator", "main.py", ["3 + 5"]).replace("\n", "\n  "))
print("-" * 30)

# 3. Running internal tests
print('run_python_file("calculator", "tests.py"):')
print("Result:")
print("  " + run_python_file("calculator", "tests.py").replace("\n", "\n  "))
print("-" * 30)

# 4. Unauthorized path (Parent directory traversal)
print('run_python_file("calculator", "../main.py"):')
print("Result:")
print("    " + run_python_file("calculator", "../main.py"))
print("-" * 30)

# 5. Non-existent file
print('run_python_file("calculator", "nonexistent.py"):')
print("Result:")
print("    " + run_python_file("calculator", "nonexistent.py"))
print("-" * 30)

# 6. Invalid file type (Not a .py file)
print('run_python_file("calculator", "lorem.txt"):')
print("Result:")
print("    " + run_python_file("calculator", "lorem.txt"))