Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> dict={"Name":["Raj","Peter","John","Kamal"],"ID":[101,102,103,106],"City":["Chennai","Coimbatore","Vellore","Ooty"]}
>>> import pandas
>>> details=pandas.DataFrame(dict)
>>> print(details)
    Name   ID        City
0    Raj  101     Chennai
1  Peter  102  Coimbatore
2   John  103     Vellore
3  Kamal  106        Ooty
>>> 