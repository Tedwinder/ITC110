

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def tablePrinter(tableData):
    i = 0;             
    while (len(str(tableData[i])) > 0):

        i += 1
  
        if (i%3==0):
            print(str(tableData[i]) + "\n");
        else:
            print(str(tableData[i]) + "\t"); 

tablePrinter(tableData);
