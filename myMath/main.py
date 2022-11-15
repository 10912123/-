from myMath import 佐助

arr = []

for i in range(5):
    arr.append(int(input('請輸入數字:')))
    
print(arr)

average = 佐助.myMean(arr)

print (f'該數列之平均數為: {average}')
