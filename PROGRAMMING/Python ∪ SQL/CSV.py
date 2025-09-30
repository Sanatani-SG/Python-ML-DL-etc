import csv
from tabulate import tabulate 
with open('names.csv','r') as c:
    r = csv.reader(c)

##    next(r)#Skips first line
    with open("new_name.csv",'w') as cs:
        w=csv.writer(cs,delimiter='\t')
    #Not Beautiful ⬇ We can access values at a fixed position by [] and use it to write another files.
        for o in r:
            w.writerow(o)
    
####    #Beautiful ⬇
####    head=["First_Name","Last_Name","Email"]
####    print(tabulate(r,headers=head,tablefmt='fancy_grid'))


    
