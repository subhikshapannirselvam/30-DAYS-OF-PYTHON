Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> dic1={"Dhoni":"CSK","Ashwin":"DC","DAVID":"SRH"}
>>> dic2={"Virat":"RCB","Watson":"CSK","Rohit":"MI"}
>>> dic1.update(dic2)
>>> print("The merged set is :",dic1)
The merged set is : {'Dhoni': 'CSK', 'Ashwin': 'DC', 'DAVID': 'SRH', 'Virat': 'RCB', 'Watson': 'CSK', 'Rohit': 'MI'}
>>> del dic1["Rohit"]
>>> print("The dict after removing is :",dic1)
The dict after removing is : {'Dhoni': 'CSK', 'Ashwin': 'DC', 'DAVID': 'SRH', 'Virat': 'RCB', 'Watson': 'CSK'}
>>> players=["Dhoni","Virat","Sachin"]
>>> runs=[55,76,98]
>>> dic=dict(zip(players,runs))
>>> print("The dictionary is :",dic)
The dictionary is : {'Dhoni': 55, 'Virat': 76, 'Sachin': 98}
>>> set={"CSK","RCB","SRH","MI","DC","KKR"}
>>> n=len(set)
>>> print("The length of set is :",n)
The length of set is : 6
>>> s1={"RCB","MI","SRH","DC"}
>>> s2={"RCB","DC","KXIP","KKR"}
>>> print("Removing the intersection of 2nd set from 1st set",s1-s2)
Removing the intersection of 2nd set from 1st set {'MI', 'SRH'}
>>> 