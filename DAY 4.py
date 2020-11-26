Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> L=[11,22,33,44,55,66,77,88]
>>> L.append(99)
>>> print(L)
[11, 22, 33, 44, 55, 66, 77, 88, 99]
>>> del L[0]
>>> print(L)
[22, 33, 44, 55, 66, 77, 88, 99]
>>> largest=max(L)
>>> smallest=min(L)
>>> print("Largest element:",largest ,"Smallest element:",smallest)
Largest element: 99 Smallest element: 22
>>> T=(1,2,3,4,5)
>>> R=reversed(T)
>>> print("The reversed tuple :",tuple(R))
The reversed tuple : (5, 4, 3, 2, 1)
>>> T1=("jan","feb","mar","apr")
>>> tuple_to_list=list(T1)
>>> print("The converted list: ",tuple_to_list)
The converted list:  ['jan', 'feb', 'mar', 'apr']
>>> 