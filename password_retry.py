# times = 3
# times = int(times)
# while True:
# 	password = input('請輸入密碼: ')
# 	if password == 'a123456':
# 		print('登入成功')
# 		break
# 	elif times != 0:
# 		times = times - 1
# 		print('密碼錯誤! 還有', times, '次機會')
# 	else:
# 		break

# 老師寫法
password = 'a123456'
i = 3 # 剩餘機會

while i > 0:
	pwd = input('請輸入密碼: ')
	if pwd == password:
		print('登入成功')
		break # 逃出迴圈
	else:
		i = i - 1
		print('密碼錯誤! 還有', i, '次機會')