from functions.get_files_info import get_files_info

# Test 1: Current Directory
print('get_files_info("calculator", "."):')
print("Result for current directory:")
# We indent the output to match the desired format
print("  " + get_files_info("calculator", ".").replace("\n", "\n  "))
print() # Add a blank line for readability

# Test 2: 'pkg' subdirectory
print('get_files_info("calculator", "pkg"):')
print("Result for 'pkg' directory:")
print("  " + get_files_info("calculator", "pkg").replace("\n", "\n  "))
print()

# Test 3: Unauthorized /bin directory
print('get_files_info("calculator", "/bin"):')
print("Result for '/bin' directory:")
# Error messages are usually single lines, so we just indent once
print("    " + get_files_info("calculator", "/bin"))
print()

# Test 4: Unauthorized parent directory traversal
print('get_files_info("calculator", "../"):')
print("Result for '../' directory:")
print("    " + get_files_info("calculator", "../"))