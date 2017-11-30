data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 
		if count % 1000 == 0:
		    print(len(data))
print('檔案讀取完了, 總共有', len(data), '筆資料')


# 如果留言有提到good的情況下，有多少機率也有提到like

# P(good) 留言有提到good的機率
good = [d for d in data if 'good' in d]
p_good = len(good) / len(data)
print('P(good)=', p_good)

# P(like) 留言有提到like的機率
like = [d for d in data if 'like' in d]
p_like = len(like) / len(data)
print('P(like)=', p_like)

# P(good|like) 留言有提到like的情況下, 也有提到good的機率
good_and_like = [d for d in data if 'good' in d and 'like' in d]
p_good_like = len(good_and_like) / len(like)
print('P(good|like)=', p_good_like)

# P(like|good) 留言有提到good的情況下，有多少機率也有提到like
p_like_good = p_good_like * p_like / p_good
print('P(like|good)=', p_like_good) # 0.32616425715164565

