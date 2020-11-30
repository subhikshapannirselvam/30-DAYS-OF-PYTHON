Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> try:  
    a,b = 100,500
    assert a == b
except AssertionError:
	print("Assertion Exception occured.")
	print("a and b are not equal.")

	
Assertion Exception occured.
a and b are not equal.
>>> try:
	x=10
	x.append(50)
except AttributeError:
	print("Attribute error occured")
	print("int don't have append attribute")

	
Attribute error occured
int don't have append attribute
>>> try:
    from time import datetime
except ImportError:
	print("Import Error occured")
	print("Imported module is not found")

	
Import Error occured
Imported module is not found
>>> try:  
    a = {1:'a', 2:'b', 3:'c'}  
    print (a[4])  
except LookupError:  
    print ("Key Error Exception Raised.")
    print("key you are trying to access is not found in the dictionary")

    
Key Error Exception Raised.
key you are trying to access is not found in the dictionary
>>> try:
	a=["a","b,","c"]
	print(a[5])
except IndexError:
	print("Index error occured")
	print("List index out of range")

	
Index error occured
List index out of range
>>> try:
	 inp = input()
	 print ('Press Ctrl+C or Interrupt the Kernel:')
except KeyboardInterrupt:
	print ('Caught KeyboardInterrupt')

	

Press Ctrl+C or Interrupt the Kernel:
>>> 
KeyboardInterrupt
>>> try:
	a=python
	print(aa)
except NameError:
	print("Name Error occured")
	print("'aa' is not defined")

	
Name Error occured
'aa' is not defined
>>> try:
	from fruit import orange
except ModuleNotFoundError:
	print("There is no module")

	
There is no module
>>> try:  
    a = 100 / 0
    print (a)
except ZeroDivisionError:  
        print ("Zero Division Exception Raised." )
        print("You can't divide a number by Zero.")

        
Zero Division Exception Raised.
You can't divide a number by Zero.
>>> try:  
    import math
    print(math.exp(1000))
except OverflowError:  
        print ("OverFlow Exception Raised.")
        print ("exp(1000) is undefined.")

        
OverFlow Exception Raised.
exp(1000) is undefined.
>>> try:
    a = 5
    b = "python"
    c = a + b
except TypeError:
    print ('TypeError Exception Raised')
    print("String and integer cannot be added")

    
TypeError Exception Raised
String and integer cannot be added
>>> try:
    print (int('Python'))
except ValueError:
	print("Value error occured")
	print("int gets unrelated datatype(value)")

	
Value error occured
int gets unrelated datatype(value)
>>> try:
   fh = open("testfile", "r")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print ("IOError: can't find file or read data")

   
IOError: can't find file or read data
>>> try:
    print "hello"
except SyntaxError:
    print("Syntax error occured")
    print("missing parantheses in call tp 'print'")
    
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("hello")?
>>> 