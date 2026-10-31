word = input("Enter the word you want to find: ")


filename = input("Enter the text file name: ")

try:
    with open(filename, "r") as file:

        count = 0

        for line_number, line in enumerate(file, start=1):

            if word.lower() in line.lower():

                print("Line", line_number, ":", line.strip())

                count += 1

        print("\nTotal matches found:", count)

except FileNotFoundError:
    print("Error: File not found.")

except PermissionError:
    print("Error: You do not have permission to open this file.")
