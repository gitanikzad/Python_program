row1=[" "," "," "]
row2=[" "," "," "]
row3=[" "," "," "]
map=[row1,row2,row3]
position=(input("Where do you want to mark?"))
#print(f"{row1}\n{row2}\n{row3}")
#column=position.split()
#print(position[0])
column= int(position[0])-1
row= int(position[1])-1
# column[0]=int(position[0])-1
# column[1]=int(position[1])-1
# # print(column)
# #
# # print(map)
#
map[row][column]='*'
print(f"{row1}\n{row2}\n{row3}")