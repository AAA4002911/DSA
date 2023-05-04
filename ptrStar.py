# Recursion pattern

while True:
    n = int(input("Enter the length limit 10-75: "))
    if n < 75 and n >= 10: break

# while True:
#     round = int(input("Enter the number of rounds 1-100: "))
#     if round < 100 and round > 0: break

def printPtr(i, n, r, round):
    if i == n and r == round:
        return 0
    if i == n: 
        printPtr(0, n, r + 1, round)
    else :
        row = ''
        for x in range(0, i):
            row += '*' + ' '
        print(row)
        printPtr(i + 1, n, r, round)
        return 0

# printPtr(0, n, 0, round)



ptr = input("Enter symbol: ")
def printPtrInfy(n, ptr):
    while True:
        for i in range(0, n):
            row = ''
            for x in range(0, i):
                row += ptr + ' '
            print(row)
        for i in range(n, 0, -1):
            row = ''
            for x in range(0, i):
                row += ptr + ' '
            print(row)

printPtrInfy(n, ptr)