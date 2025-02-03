import pyda

pyda.create("Table",3,4,1)
pyda.defheadcol(["S.No","Name","Age","ID"])
pyda.addcols([[1,"Kunsh",18,"24BCE1282"],[2,"Swasthik",19,"24BLC1283"],[3,"Rapeansh",18,"24BEE1284"]])
pyda.endtable()
pyda.create("Table1",3,4,1)
pyda.defheadcol(["S.No","Name","Age","ID"])
pyda.addcols([[1,"Kunsh",18,"24BCE1282"],[2,"Swasthik",19,"24BLC1283"],[3,"Rapeansh",18,"24BEE1284"]])
pyda.endtable()

pyda.show("Table")
pyda.search('Table','1')
pyda.showstruct("Table")

pyda.clear()