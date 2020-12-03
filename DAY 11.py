Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def merge(l1,l2):
	result_list=tuple(zip(l1,l2))
	return result_list

>>> l1=["CSK","MI","RCB"]
>>> l2=["Dhoni","Rohit","Virat"]
>>> print("The merged tuple:",merge(l1,l2))
The merged tuple: (('CSK', 'Dhoni'), ('MI', 'Rohit'), ('RCB', 'Virat'))
>>> given_list=[12,21,13,31,14,41,15]
>>> given_range=range(1,8)
>>> result=tuple(zip(given_list,given_range))
>>> print("The resultant tuple:",result)
The resultant tuple: ((12, 1), (21, 2), (13, 3), (31, 4), (14, 5), (41, 6), (15, 7))
>>> list_city=["India","America","Australlia","China","New york","Paris","Japan","Thailand","Srilanka"]
>>> list_city.sort()
>>> print("The sorted list:",list_city)
The sorted list: ['America', 'Australlia', 'China', 'India', 'Japan', 'New york', 'Paris', 'Srilanka', 'Thailand']
>>> numbers = [11,12,13,14,15,16,17,18,19,20]
>>> filter_function = filter(lambda x: x % 2 == 1, numbers)
>>> print(list(filter_function))
[11, 13, 15, 17, 19]
>>> 