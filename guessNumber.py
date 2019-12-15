import random
print("終極密碼:數字介於1 ~ 100")
puzzle = random.randint(1, 100)
count = 0
min = 1
max = 100
while True:
	
	guess_number = input('請輸入您猜的數字: ')
	guess_number = int(guess_number)
	if(guess_number <= min or guess_number >= max):
		print("輸入錯誤，請重新輸入", min, "到", max, "間的數字")
	else:
		count += 1
		if (guess_number == puzzle):
			print("猜對了")
			print("你總共猜了", count, "次")
			break
		else:
			if(guess_number > puzzle):
				max = guess_number
				print(min, "到", max)
			else:
				min = guess_number
				print(min, "到", max)
	