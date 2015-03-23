print('Welcome To Our Temp Conversion Program')
temp = input("What temp would you like to convert to? Type Celsius or Fahrenheit. ").lower().strip()


if temp[0] == 'c':
	userstemp = float(input("What is your temp to be converted. "))
	cel = round((userstemp - 32) * 5 / 9, 1)
	print("Your temp in Celsius is {}".format(cel))
elif temp[0] == 'f':
	userstemp = float(input("What is your temp to be converted. "))
	fah = round(userstemp * 9 / 5 + 32, 1)
	print("Your temp in Fahrenheit is {}".format(fah))
else:
	print("Whoops Something went wrong")


