Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> try:
	age=int(input("Please enter your age: "))
	if age<18:
		print("you are minor.")
	else:
		print("you are major.")
except ValueError:
	print("Enter a valid number.")
finally:
	print("Completed!")

	
Please enter your age: 19
you are major.
Completed!
>>> 