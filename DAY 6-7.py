def find( number_of_days ):
	year = int(number_of_days / 365) 
	week = int((number_of_days % 365) /7) 
	days = (number_of_days % 365) % 7
	print("The age is",year,"years",week,"weeks",days,"days")
number_of_days = int(input("Enter number of days:"))
find(number_of_days)
