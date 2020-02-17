import sys


while True:

    binary = input("Binary: ")

    output = 0
    count = 0

    if binary == "q":
        sys.exit()

    if binary == "0" or binary == "1":
        print(binary)
        sys.exit()

    else:
        while binary != "":
            output += int(binary[-1]) * (2 ** count)
            binary = binary[:-1]
            count += 1

    print(output, end="\n\n")
