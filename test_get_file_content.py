from functions.get_file_content import get_file_content

# 1. Lorem Ipsum (Truncation test)
print('get_file_content("calculator", "lorem.txt"):')
print("Result for 'lorem.txt':")
print("  " + get_file_content("calculator", "lorem.txt").replace("\n", "\n  "))
print()

# 2. main.py
print('get_file_content("calculator", "main.py"):')
print("Result for 'main.py':")
print("  " + get_file_content("calculator", "main.py").replace("\n", "\n  "))
print()

# 3. pkg/calculator.py
print('get_file_content("calculator", "pkg/calculator.py"):')
print("Result for 'pkg/calculator.py':")
print("  " + get_file_content("calculator", "pkg/calculator.py").replace("\n", "\n  "))
print()

# 4. /bin/cat (Should return error)
print('get_file_content("calculator", "/bin/cat"):')
print("Result for '/bin/cat':")
print("    " + get_file_content("calculator", "/bin/cat"))
print()

# 5. pkg/does_not_exist.py (Should return error)
print('get_file_content("calculator", "pkg/does_not_exist.py"):')
print("Result for 'pkg/does_not_exist.py':")
print("    " + get_file_content("calculator", "pkg/does_not_exist.py"))
