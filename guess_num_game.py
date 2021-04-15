import random
start = input('請決定隨機數字範圍開始值:')
end = input('請決定隨機數字範圍結束值:')
start = int(start)
end = int(end)

r = random.randint(start, end) #1~100 產生隨機數
count = 0
while True:
	count += 1 #是 count = count + 1 的快寫法
	num = input('請猜數字(1~100): ')
	num = int(num)
	if num == r:
		print('你猜中了!')
		print('這是你猜的第',count,'次')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	print('這是你猜的第',count,'次')