# list1 = [75]
# list2 = [95, 64]
# list3 = [17, 47, 82]
# list4 = [18, 35, 87, 10]
# list5 = [20, 04, 82, 47, 65]
# list6 = [19, 01, 23, 75, 03, 34]
# list7 = [88, 02, 77, 73, 07, 63, 67]
# list8 = [99, 65, 04, 28, 06, 16, 70, 92]
# list9 = [41, 41, 26, 56, 83, 40, 80, 70, 33]
# list10 = [41, 48, 72, 33, 47, 32, 37, 16, 94, 29]
# list11 = [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14]
# list12 = [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57]
# list13 = [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48]
# list14 = [63, 66, 04, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31]
# list15 = [04, 62, 98, 27, 23, 09, 70, 98, 73, 93, 38, 53, 60, 04, 23]


def recSumAtRow(rowData, rowNum):
    # iterate over the given row
    for i in range(len(rowData[rowNum])):
        
        rowData[rowNum][i] += max([rowData[rowNum+1][i],rowData[rowNum+1][i+1]])
    
    if len(rowData[rowNum])==1: return rowData[rowNum][0]
    
    else: return recSumAtRow(rowData, rowNum-1)
rows = []
with open('problem-18-data') as f:
    for line in f:
        rows.append([int(i) for i in line.rstrip('\n').split(" ")])
 
 

result = recSumAtRow(rows, len(rows)-2)

 
 
print(result)
