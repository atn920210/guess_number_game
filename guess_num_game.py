import random

r = random.randint(1, 100) #1~100 產生隨機數
while True:
	num = input('請猜數字(1~100): ')
	num = int(num)
	if num == r:
		print('你猜中了!')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')