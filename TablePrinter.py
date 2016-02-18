
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def tablePrinter(tableData):
    i = 0;
    
    for i in range(0,len(tableData)):
        #colWidths = [i] * len(tableData);
        p=0;
        for p in range(0,len(tableData[i])):
            if ((p/3).is_integer() and p!=0):
                print((str(tableData[i][p])).rjust(5), end="\n");
            else:
                print((str(tableData[i][p])).rjust(5), end="\t\t"); 
        
        
tablePrinter(tableData);

