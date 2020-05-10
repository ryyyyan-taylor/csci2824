def mega_digit (n, k) :
    x = ""

    for i in range (0, k) :
        x += str(n)
    
    out = 0
    
    while (True) :
        for digit in x :
            out += int(digit)
            
        if (len(str(out)) == 1) : 
            break
        x = str(out)
        out = 0
        
    return out

print(mega_digit(12, 2))
print(mega_digit(321, 3))
print(mega_digit(98765432, 1))
