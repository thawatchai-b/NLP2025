from math import inf #infinity


thai_vocab = ["ไ","ป","ห","า","ม","เ","ห","ส","ี","ไป","หา","หาม","เห","สี","มเหสี","!"]
input_text = "ไปหามเหสี!"

c = input_text

d  =[[None]*len(c) for _ in range(len(c))]

for i in range(len(c)):
    for j in range(i,len(c)):
        word = c[i:j+1]
        if i == 0 and c[0:j+1] in thai_vocab:
            print(i, j)
            d[i][j] = 1


print(min(d[i]))