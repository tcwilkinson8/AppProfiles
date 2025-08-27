input_string = input("type a String:")

print("\nString Manipulation Menu:")
print("1. Convert to Uppercase")
print("2. Convert to Lowercase")
print("3. Slice the String")
print("4. Calculate sting length")
print("5. Loop through characters")

choice = int(input("Enter your choice (1-5)"))

if choice == 1:
    result = input_string.upper()
    print("Uppercase:, result")
elif choice == 2:
    result = input_string.lower()
    print("Lowercase:", result)
elif choice == 3:
    start = int(input("Enter start index:"))
    end = int(input("Enter end index:"))
    result = input_string[start:end]
    print("Sliced String:", result)
elif choice == 4:
    result = len(input_string)
    print("String Length:", result)
elif choice == 5:
    print("Characters:")
    for char in input_string:
        print(char)

else:
    print("Invalid choice")
