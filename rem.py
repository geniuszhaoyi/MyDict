import os,sys
import json
import random
import copy

mydict={}

def explain(word):
    global mydict
    if word in mydict:
        return mydict[word]
        
def worddst(a, b):
    __author__ = 'xanxus'  
    s1, s2 = a, b
    m, n = len(s1), len(s2)  
    colsize, matrix = m + 1, []  
    for i in range((m + 1) * (n + 1)):  
        matrix.append(0)  
    for i in range(colsize):  
        matrix[i] = i  
    for i in range(n + 1):  
        matrix[i * colsize] = i  
    for i in range(n + 1)[1:n + 1]:  
        for j in range(m + 1)[1:m + 1]:  
            cost = 0  
            if s1[j - 1] == s2[i - 1]:  
                cost = 0  
            else:  
                cost = 1  
            minValue = matrix[(i - 1) * colsize + j] + 1  
            if minValue > matrix[i * colsize + j - 1] + 1:  
                minValue = matrix[i * colsize + j - 1] + 1  
            if minValue > matrix[(i - 1) * colsize + j - 1] + cost:  
                minValue = matrix[(i - 1) * colsize + j - 1] + cost  
            matrix[i * colsize + j] = minValue  
    return matrix[n * colsize + m]
def printnearest(word,n=6):
    words=[]
    for k,v in mydict.items():
        if worddst(k,word)<=3:
            words.append(k)
            if len(words)>=n: break
            
    if len(words)<=2:
        for k,v in mydict.items():
            words.append(k)
        random.shuffle(words)
        words=words[:6]
    
    if word not in words: words.append(word)
    random.shuffle(words)
    for w in words:
        print '>>',w

def rem(d,wl):
    wordlist=copy.deepcopy(wl)

    Recite_Num = 3
    
    print 
    print '-'*35
    print 'WORD LIST',d
    print '-'*35
    
    for word in wordlist:
        while True:
            print '-'*20
            print '::',word,'::'
            print explain(word)
            mark=False
            for i in range(Recite_Num):
                inp=raw_input(str(i)+'\t')
                if inp!=word:
                    mark=True
                    break
            if not mark: break
        
    random.shuffle(wordlist)
    
    for word in wordlist:
        print '-'*20
        print explain(word)
        printnearest(word)
        while True:
            w=raw_input('word: ')
            if w!=word:
                print 'Wrong! ::',word,'::'
                # adddif(w)
            else:
                print 'Correct!'
                break
    
def main():
    global mydict

    f=open('gre3000.dict')
    ls=f.readlines()
    f.close()
    
    for l in ls:
        sp=l.find('\t')
        key=l[:sp]
        val=l[sp+1:]
        mydict[key]=val
    
    tws=[]
    
    print 'Type in today\'s words'
    while True:
        try:
            word=raw_input('word: ')
            ex=explain(word)
            if ex!=None:
                tws.append(word)
                print ex
        except EOFError:
            break
            
    f=open('wordhistory.json')
    ds=json.loads(f.read())
    f.close()
    
    ds.append(tws)
    
    f=open('wordhistory.json','w')
    f.write(json.dumps(ds))
    f.close()
    
    x=[0,1,2,4,7,15]
    x.reverse()
    
    lends=len(ds)
    rem(lends-1,ds[lends-1])
    for xi in x:
        if lends-1-xi>=0: rem(lends-1-xi,ds[lends-1-xi])
        
    print '-'*35
    print 'CONGRATULATIONS! '
    print '-'*35

import readline
import rlcompleter
import atexit
def reg():
    histfile = os.path.join(os.environ['HOME'], '.pythonhistory')
    try:
        readline.read_history_file(histfile)
    except IOError:
        pass
    atexit.register(readline.write_history_file,histfile)

if __name__=='__main__':
    reg()
    main()
