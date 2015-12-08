SIZE = 6


for row in range(0, SIZE):
    for col in range(1, row + 1):
        print " ",

    for col in range(row + 2, SIZE + 1):
        print "#",
        
    for col in range(row, SIZE):
        print "#", 

    print
