# Program extracting first column 
import xlrd 
from collections import Counter
import plotly.graph_objects as go
loc = ("./2000_translated.xlsx") 
  
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
# sheet.cell_value(1, 1) 

list = []
for i in range(sheet.nrows): 
    list.append(sheet.cell_value(i, 2))

listKey = []
listValue = []
for i in Counter(list).values():
    listValue.append(i)

for i in Counter(list).keys():
    listKey.append(i)

fig = go.Figure(
    data=[go.Bar(x=listKey,y=listValue)],
    layout_title_text="A Figure Displayed with fig.show()"
)
fig.show()