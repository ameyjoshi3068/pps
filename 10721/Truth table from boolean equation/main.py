equation=(input("Enter the logic equation indicate not by ~\nand by +\nor by .\n>>"))
equation.strip
operators=("~","+",".")
columns=[]
for i in equation:
    if i not in operators:
        columns.append(i)
varcount=len(columns)
columns.append(equation)
from prettytable import PrettyTable
truthTable=PrettyTable()

if varcount<1:
    truthTable.add_column(columns[0],([0,1]))
    varvalues=[0,1]
elif varcount<2:
    truthTable.add_column(columns[0],([0,0,1,1]))
    truthTable.add_column(columns[1],([0,1,0,1]))
    varvalues=[[0,0,1,1],[0,1,0,1]]
elif varcount<3:
    truthTable.add_column(columns[0],([0,0,0,0,1,1,1,1]))
    truthTable.add_column(columns[1],([0,0,1,1,0,0,1,1]))
    truthTable.add_column(columns[2],([0,1,0,1,0,1,0,1]))
    varvalues=[[0,0,0,0,1,1,1,1],[0,0,1,1,0,0,1,1],[0,1,0,1,0,1,0,1]]
else:
    varvalues=[]
    for i in range(varcount):
        column=([0 for i in range(2**(varcount-(i+1)))]+[1 for i in range(2**(varcount-(i+1)))])*(2**i)
        truthTable.add_column(columns[i],(column))
        varvalues.append(column)

# equation=equation.replace("~","~")
equation=equation.replace("+","|")
equation=equation.replace(".","&")
print()
column=[]
   
for i in varvalues[0]:
    count=0
    for j in columns[:-1]:
        print(bin(varvalues[count][i]))
        exec("%s = %s" % (j,bin(varvalues[count][i])))
        count+=1
    # count==0
    
    # for i in equation:
    #     if i=="!":
    #         val=equation[count+3]
    #         print("val=",val)
    #         print("z",z)
    #         ans=eval("!"+val)
    #         print("ans=",ans)
    #         equation= equation.replace(f"!{val}",str(ans))
    ans=(eval(equation))
    column.append(ans)

truthTable.add_column(columns[varcount],(column))
print(truthTable)