# 讀取檔案
def readfile(filename):
	file_list = []
	with open(filename, 'r') as f:
		for line in f:
			file_list.append(line)
			if len(file_list) % 10000 == 0:
				print('檔案讀取中，目前讀取第', len(file_list), '筆資料')
		return file_list


# 留言平均字數
def aver_len(datalist):
	sum = 0
	for data in datalist:
		sum += len(data)
	print('共', len(datalist), '筆留言，其每筆留言平均長度為', sum / len(datalist), '個字')


# 算出x字數的有幾筆
def words_counter(datalist, x):
	count = 0
	for data in datalist:
		if len(data) < x:
			count += 1
	print('留言字數小於', x, '字的有', count,"筆")


def is_empty(datalist):
	if datalist == None:
		return True
	else:
		return False

# 取消此寫法，直接用查字典的方法
# def is_repeat(dic_list, key, value):
# 	count = 0
# 	for dic in dic_list:
# 		count += 1
# 		if dic[key] == value:
# 			return True
# 		elif count == len(dic_list): ##注意這裡不能直接用else, 否則只要第一筆不重複就直接False
# 			return False


def add_dic_count(dic_list, key, value):
	for dic in dic_list:
		if dic[key] == value:
			dic['count'] += 1


def words_dics(datalist):
	dics = {}
	for data in datalist:
		# words = data.split(' ') 會切出空字串
		words = data.split() #預設值會跳過空格
		for word in words:
			if word in dics:
				dics[word] += 1
			else:
				dics[word] = 1
				
	for word in dics:
		if dics[word] > 1000:
			print(word, dics[word])	
	print(len(dics))		
	return dics

			
				



# def hot_word(dics):
# 	for word in dics:
# 		if dics[word] == max(dics, key = dics.get):
# 			print(dics[word])
# 	print(max(dics, key = dics.get), dics[max(dics, key = dics.get)])

			





def main():
	reviews = readfile('reviews.txt')
	aver_len(reviews)
	words_counter(reviews, 100)
	dics = words_dics(reviews)
	while True:
		word = input('輸入想要查的字或q離開')
		if word == 'q':
			print('感謝使用')
			break
		else:
			# 方法一:異常處理
			# try:
			# 	print(word, '出現', dics[word], 次)
			# except KeyError:
			# 	print('查無此字')

			# 方法二:get function
			print(word, dics.get(word, '查無此字'))

	# hot_word(dics)print(dics)
	# print('最常出現的字為', dics[max_index]['word'], '出現', max_count, '次')	

main()
# reviews = readfile('reviews.txt')


# testlist = hot_words(reviews, 0, 1)
# print(testlist)
# for dic in testlist:
# 	if dic['word'] == 'I':
# 		print('True') 
# 	else: 
# 		print('False') 
# print(testlist)













# reviews = []
# sum_length = 0
# count = 0
# with open('reviews.txt', 'r') as f:
# 	for line in f:
# 		sum_length += len(line)
# 		reviews.append(line)
		
# reviews_length = len(reviews)
# averave_length = sum_length / reviews_length
# print('檔案讀取完了，總共有',len(reviews),'筆資料。其留言平均長度為', averave_length, '個字')

# sort_reviews = []
# for data in reviews:
# 	if len(data) < 100:
# 		sort_reviews.append(data)
# print('留言小於100字的共有', len(sort_reviews), '筆資料')
