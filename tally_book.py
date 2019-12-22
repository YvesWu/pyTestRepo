# 讀取檔案
products = []
with open('tallyBook.csv', 'r') as f:
	for line in f:
		if '商品, 價錢' in line:
			continue
		product, price = line.strip().split(',') 
		products.append([product, price])
print(products)

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