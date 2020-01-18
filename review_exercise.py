data = []
count = 0
with open('reviews.txt','r') as f:
    for line in f:
        data.append(line)
        count += 1 
        if count % 10000 == 0:
            print(len(data))
print('檔案讀取完了, 共有', len(data), '筆資料')

sum_len = 0
for d in data:
    sum_len += len(d) #sum_len = sum_len + len(d)

average = sum_len/len(data)
print('留言的平均長度為', average)

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('一共有', len(new),'筆留言長度小於100')

good = []

for d in data:
    if 'good' in d:
        good.append(d)
print('一共有', len(good), '筆好的留言')

#       運算   變數  清單      篩選條件
#good = [d for d in data if 'good' in d]

bad = ['bad' in d for d in data]

bad = []
for d in data:
    bad.append('bad' in d)
    
