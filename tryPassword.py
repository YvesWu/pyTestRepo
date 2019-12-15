password = 'a123456'
count = 3
while count > 0:
	user_password = input('請輸入密碼:')
	if (password == user_password):
		print('登入成功')
		break
	else:
		count -= 1
		print('密碼錯誤')
		if(count != 0):
			print('你還有', count, '次機會' )
	