row = int(input("Enter no of rows::"))
for i in range (1, row+1):
    for j in range (row):
        print((i+j)%row +1, end='')
    print('')




