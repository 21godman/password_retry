times = 3
times = int(times)
while True:
	password = input('請輸入密碼: ')
	if password == 'a123456':
		print('登入成功')
		break
	elif times != 0:
		times = times - 1
		print('密碼錯誤! 還有', times, '次機會')
	else:
		break