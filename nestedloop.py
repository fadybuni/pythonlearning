

rows =  int(input("enter the number of rows: "))
columns = int(input("enter the number of columns: "))
symbol = input("Enter a symbol to use: ")
for j in range(rows):
    for x in range(columns):
        print(symbol, end ="")
    print()
