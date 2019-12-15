
while True:
	celsius = input("input the Celsius: ")
	if celsius == "":
		break
	else:
		celsius = float(celsius)
		fahrenheit = celsius * 9 / 5 + 32
		print("fahrenheit is ", fahrenheit)