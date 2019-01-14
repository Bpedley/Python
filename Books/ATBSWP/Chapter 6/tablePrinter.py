tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    # create a new list of 3 "0" values: one for each list in tableData
    colWidths = [0] * len(table)
    # search for the longest string in each list of tableData
    # and put the numbers of characters in the new list
    for list in range(len(table)):
        for item in table[list]:
            if colWidths[list] < len(item):
                colWidths[list] = len(item)

    # "rotate" and print the list of lists
    for x in range(len(table[0])):
        for y in range(len(table)):
            print(table[y][x].rjust(colWidths[y]), end = ' ')
        print()

printTable(tableData)
