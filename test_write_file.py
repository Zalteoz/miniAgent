from functions.write_file import write_file

# Test 1: Writing to a file in the root of the working directory
print('write_file("calculator", "lorem.txt", "wait, this isn\'t lorem ipsum"):')
print("Result:")
print("    " + write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
print()

# Test 2: Writing to a file in a subdirectory (Tests the makedirs logic)
print('write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"):')
print("Result:")
print("    " + write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
print()

# Test 3: Unauthorized path (Security check)
print('write_file("calculator", "/tmp/temp.txt", "this should not be allowed"):')
print("Result:")
print("    " + write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))