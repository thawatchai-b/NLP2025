from math import inf #infinity

def maximal_matching(c):
    #Initialize an empty 2D list
    d  =[[None]*len(c) for _ in range(len(c))]

    ####FILL CODE HERE####
    for i in range(len(c)): #row 0..len(c)
        print(i)
        for j in range(i+1):  #col
            inVocab = (c[i:j] in thai_vocab)             
    
            print(i, j, c[i:j])
            if i==0 and inVocab:
                d[i,j] = 1
            elif inVocab:
                d[i,j] = 1 + min(d[:i-1])
            else:                
                d[i,j] = inf

    return d


if __file__ == "__main__":
    thai_vocab = ["ไ","ป","ห","า","ม","เ","ห","ส","ี","ไป","หา","หาม","เห","สี","มเหสี","!"]
    input_text = "ไปหามเหสี!"

    out = maximal_matching(input_text)
    for i in range(len(out)):
        print(out[i],input_text[i])