#檢查檔案
import os #operating system
products = []
if os.path.isfile('tallyBook.csv'):
	print('檔案存在')
	# 讀取檔案
	with open('tallyBook.csv', 'r') as f:
		for line in f:
			if '商品, 價錢' in line:
				continue
			product, price = line.strip().split(',') #spilt(',') 字串依逗號分隔成清單
			products.append([product, price])
	print(products)
else:
	print('檔案不存在')



# 使用者輸入
while True:
	product = input('請輸入商品名稱，或q離開: ')
	if product == 'q':
		break
	price = input('請輸入商品價錢(NTD): ')
	price = int(price)
	products.append([product, price])

# 印出明細
for product in products:
	print(product)

# 儲存至csv檔
with open('tallyBook.csv', 'w') as f:
	f.write('商品, 價錢\n')
	for product in products:
		f.write(product[0] + ',' + str(product[1]) + '\n')