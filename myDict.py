import os,sys

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

def wordcmp(a, b):
    #sys.stderr.write(a+' '+b+"\n")
    if a==b: return True
    if len(a)==0 or len(b)==0: return False
    if a[0]=='*':
        mark=False
        for i in range(len(b)-len(a)+2):
            #sys.stderr.write(str(len(b)-len(a)+1)+' '+str(i)+"\n")
            if wordcmp(a[1:],b[i:]):
                mark=True
                break
        return mark
    elif a[0]=='?':
        return wordcmp(a[1:],b[1:])
    else:
        if a[0]==b[0]:
            return wordcmp(a[1:],b[1:])
        else: 
            return False

def dictfind(Dicts, a):
    WORDS_MAX_DST=1
    if a.find('*')>=0 or a.find('?')>=0:
        ans=[]
        for d,val in Dicts.items():
            if wordcmp(a,d): ans.append(d)
        return ans
    elif a in Dicts:
        return [a]
    else:
        ans=[]
        for d,val in Dicts.items():
            wd=worddst(a,d)
            if wd<=WORDS_MAX_DST: ans.append((wd,d))
        ans=sorted(ans)
        return [val for (fwd,val) in ans[:5]]

#---------------------------------------------

def getDscp(Dicts, a):
    chartype = sys.getfilesystemencoding()

    print a
    print Dicts[a].decode('utf-8').encode(chartype)

def getdict(Dicts, a): 
    for (desc,Dict) in Dicts:
        print '-'*20
        print 'Words from: <<',desc,'>>'
        xs=dictfind(Dict, a)
    
        for x in xs:
            getDscp(Dict,x)
            
    print '-'*20

def dictload(path):
    ansdict={}

    f=open(path)
    ls=f.readlines()
    f.close()
    
    for l in ls:
        sp=l.find('\t')
        key=l[:sp]
        val=l[sp+1:]
        ansdict[key]=val
    
    return ansdict

import readline
import rlcompleter
import atexit

def main():
    #tab completion
    #readline.parse_and_bind('tab: complete')
    #history file
    histfile = os.path.join(os.environ['HOME'], '.pythonhistory')
    try:
        readline.read_history_file(histfile)
    except IOError:
        pass
    atexit.register(readline.write_history_file,histfile)
    
    f=open('/home/zhaoyi/workspace/myDict/dicts.conf')
    ls=f.readlines()
    f.close()
    Dicts=[]
    for l in ls:
        x=l.split()
        if len(x)<=0: continue
        Dicts.append((x[0],dictload(x[1])))

    if len(sys.argv)>1:
        for a in sys.argv[1:]:
            getdict(Dicts.lower(),a.lower())
    else:
        while 1:
            try:
                word=raw_input('Enter word to search: ')
                getdict(Dicts,word.lower())
            except EOFError:
                break
    print '\nBye'
    
if __name__=='__main__':
    main()
