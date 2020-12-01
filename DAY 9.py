Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ans=lambda x,y:x*y
>>> print("The answer is:",ans(99,80))
The answer is: 7920
>>> from functools import reduce
>>> fibseries=lambda n:reduce(lambda x,_:x+[x[-1]+x[-2]],range(n-2),[0,1])
>>> print("The fibonacci series is",fibseries(8))
The fibonacci series is [0, 1, 1, 2, 3, 5, 8, 13]
>>> alist=[1,2,3,4,5]
>>> n=5
>>> multiplies_numbers=list(map(lambda number:number*n,alist))
>>> print("Original list is",alist)
Original list is [1, 2, 3, 4, 5]
>>> print("After multiplied with",n,":",' '.join(map(str,multiplies_numbers)))
After multiplied with 5 : 5 10 15 20 25
>>> list1=[8,18,23,45,81,18,98,14,15]
>>> ans=list(filter(lambda x:x%9==0,list1))
>>> print("Numbers of the list that are divisble by 9:",ans)
Numbers of the list that are divisble by 9: [18, 45, 81, 18]
>>> list2=[11,12,13,14,15,16,17,18,19,10]
>>> even_ct=len(list(filter(lambda x:x%2==0,list2)))
>>> print("Number of even numbers in the list are",even_ct)
Number of even numbers in the list are 5
>>> 