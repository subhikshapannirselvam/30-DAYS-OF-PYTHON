Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
>>> def specific_patterns(text):
	pattern='^[a-zA-Z0-9]*$'
	if re.search(pattern,text):
		return "This string has certain characters only."
	else:
		return "This string has invalid characters."

	
>>> print(specific_patterns("Pass123"))
This string has certain characters only.
>>> print(specific_patterns("98!@:)"))
This string has invalid characters.
>>> import re
>>> def text_match(text):
	patterns='ab.*$'
	if re.search(patterns,text):
		return "This string matches the pattern"
	else:
		return "This string doesn't match"

	
>>> print(text_match("Cab"))
This string matches the pattern
>>> print(text_match("dog"))
This string doesn't match
>>> import re
>>> def end_num(string):
	text=re.compile(r".*[0-9]$")
	if text.match(string):
		return "This string contains a number at end."
	else:
		return "This string doesn't contain a number at end."

	
>>> print(end_num("Pass123"))
This string contains a number at end.
>>> print(end_num("rajesh"))
This string doesn't contain a number at end.
>>> import re
>>> results = re.finditer(r"([0-9]{1,3})", "The points of the four teams are 8,10,300,9")
>>> for n in results:
     print(n.group(0))

     
8
10
300
9
>>> import re
>>> def text_match(text):
	pattern='^[A-Z]*$'
	if re.search(pattern,text):
		return "This string contains only Uppercase."
	else:
		return "This doesn't contain only uppercase."

	
>>> print(text_match("REGULAREXPRESSION"))
This string contains only Uppercase.
>>> print(text_match("Regularexpression"))
This doesn't contain only uppercase.
>>> 