row1 = ['📦', '📦', '📦']
row2 = ['📦', '📦', '📦']
row3 = ['📦', '📦', '📦']
map = [row1, row2, row3]

position = input("Where you want to place the treassure ? ")
col = int(position[0])
row = int(position[1])

""" if row == 1:
   row1[col -1] = 'x'
elif row == 2:
  row2[col - 1] = 'x'
elif row == 3:
  row3[col - 1] = 'x'
else:
  print("invalid index")
 """
 
""" selected_row = map[row - 1]
selected_row[col - 1] = 'x' """

map[row - 1] [col - 1] = 'X'

print(f"{row1} \n{row2} \n{row3}") 
