import openpyxl 
from string import ascii_uppercase as alf
 
f = openpyxl.load_workbook("18_7620.xlsx") #change it
 
data = [[0 for _ in range(20)] for _ in range(20)]
 
sheet = f[f.sheetnames[0]]
 
for y in range(20):
    for x in range(20): 
        if y == 0 or sheet[f"{alf[x]}{y}"].border.bottom.style!=None:
            data[y][x] = data[y][x-1] + sheet[f"{alf[x]}{y+1}"].value
 
        elif x == 0 or sheet[f"{alf[x-1]}{y+1}"].border.right.style!=None:
            data[y][x] = data[y-1][x] + sheet[f"{alf[x]}{y+1}"].value
            
        else:
            data[y][x] = max(data[y-1][x], data[y][x-1]) + sheet[f"{alf[x]}{y+1}"].value
        
for y in range(20):
    print(*data[y])
