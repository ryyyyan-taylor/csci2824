import sys


while True:

    In = input("Decimal: ")
    output = ""

    if In == "q":
        sys.exit()

    dec = int(In)
    if dec == 0 or dec == 1:
        print(dec)
        continue

    else:
        while dec >= 1:
            if dec % 2 == 0:
                output = "0" + output
                dec = dec / 2
                continue
            else:
                output = "1" + output
                dec = (dec - 1) / 2

    print(output + "\n")
