reviews = []
sum_length = 0
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		sum_length += len(line)
		reviews.append(line)
		
reviews_length = len(reviews)
averave_length = sum_length / reviews_length
print('檔案讀取完了，總共有',len(reviews),'筆資料。其留言平均長度為', averave_length, '個字')