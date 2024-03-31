times = 3 # 剩餘機會
times = int(times)
password = 'a123456'
while True:
	password = input('請輸入密碼: ')
	if pwd == password:
		print('登入成功')
		break # 逃出迴圈
	elif times != 0:
		times = times - 1
		print('密碼錯誤! 還有', times, '次機會')
	else:
		break

老師寫法
while True:
	password = input('請輸入密碼: ')
	if pwd == password:
		print('登入成功')
		break # 逃出迴圈
	else:
		times = times - 1
		print('密碼錯誤! 還有', times, '次機會')
		if times == 0:
			break