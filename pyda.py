row=0;col=0;name=[];i=0;tabname="";count=0;primec=0;d={}

import csv;import os;import atexit

CSV_DIR = os.path.join(os.path.expanduser("~"), "my_csv_files")
os.makedirs(CSV_DIR, exist_ok=True)

def clear_all_csvs():
    for filename in os.listdir(CSV_DIR):
        if filename.endswith(".csv"):
            filepath = os.path.join(CSV_DIR, filename)
            try:
                os.remove(filepath)
            except:
                pass

clear_all_csvs()

def create(n,a,b,c):
    global primec
    primec=c
    global count
    global tabname
    tabname=n
    nm=os.path.join(CSV_DIR, tabname+".csv")
    global name
    global i
    global row
    global col
    global d
    col=b;row=a;
    i=0
    if os.path.exists(nm):
        os.remove(nm)
    if n in name:
        print("Table Name Aldready Exists")
    else:
        name.append(n)
        d[n]="{}x{}".format(a,b)

def chckcol(a):
    global col
    if len(a)==col:
        return 1
    else:
        return """Attribute Error: Please Ensure No.of Coloumns is
            equal to no.of coloumns defined previously"""

def addcol(a):
    global tabname
    nm=os.path.join(CSV_DIR, tabname+".csv")
    global i
    global row
    if i<row:
        with open(nm,"a+", newline='') as fh:
            fhwriter=csv.writer(fh)
            fhwriter.writerow(a)
        i+=1
    else:
        print("Attribute Error: The no.of Rows defined is : ",row)

def addcols(a):
    global i
    global row
    global tabname
    nm=os.path.join(CSV_DIR, tabname+".csv")
    if i<row:
        if len(a)==row:
            with open(nm,"a+", newline='') as fh:
                fhwriter=csv.writer(fh)
                fhwriter.writerows(a)
        else:
            print("Attribute Error: Number of rows in input does not match the defined number of rows")
    else:
        print("Attribute Error: The no.of Rows defined is : ",row)

def addhcol(a):
    global tabname
    nm=os.path.join(CSV_DIR, tabname+".csv")
    with open(nm,"w+", newline='') as fh:
        fhwriter=csv.writer(fh)
        fhwriter.writerow(a)

def defheadcol(a):
    global row
    global col
    chkcol=chckcol(a)
    if chkcol==1:
        addhcol(a)
    else:
        print(chkcol)

def endtable():
    row=0;col=0;name=[];i=0;tabname=""

def chck():
    print(name)

def show(a):
    nm=os.path.join(CSV_DIR, a+".csv")
    try:
        with open(nm,'r') as fh:
            csvreader=csv.reader(fh)
            for i in csvreader:
                if len(i)==0:
                    pass
                else:
                    print(i)
    except:
        pass

def search(a,b):
    global primec
    primec-=1
    nm=os.path.join(CSV_DIR, a+".csv")
    try:
        with open(nm,'r') as fh:
            csvreader=csv.reader(fh)
            for i in csvreader:
                if len(i)==0:
                    pass
                else:
                    if i[primec]==b:
                        print("The data found is - ",end=' ')
                        print(i)
                    else:
                        pass
    except:
        pass

def showstruct(a):
    global d
    print("The Structure of ",a," is : ",d.get(a))

def clear():
    global name
    global d

    for table_name in list(name):
        nm = os.path.join(CSV_DIR, table_name + ".csv")
        if os.path.exists(nm):
            os.remove(nm)
            name.remove(table_name)
            try:
                del d[table_name]
            except KeyError:
                pass

    name = []
    d = {}

atexit.register(clear_all_csvs)