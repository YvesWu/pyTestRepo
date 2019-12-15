country = input("請輸入國家: ")
if country == "台灣" or country == "美國":
	age = input("請輸入年齡(歲): ")
	age = int(age)
	if country == "台灣":
		if age >= 18:
			print("你可以考駕照")
		else:
			print("你不可以考駕照")
	elif country == "美國":
		if age >= 16:
			print("你可以考駕照")
		else:
			print("你不可以考駕照")
else:
	print("你只能輸入台灣或美國")