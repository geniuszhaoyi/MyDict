import os,sys

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

def dictfind(Dictionary, a):
    if a.find('*')>=0 or a.find('?')>=0:
        ans=[]
        for d,val in Dictionary.items():
            if wordcmp(a,d): ans.append(d)
        return ans
    elif a in Dictionary:
        return [a]
    else:
        return []

#---------------------------------------------

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

def getDscp(Dictionary, a):
    chartype = sys.getfilesystemencoding()

    print a
    print Dictionary[a].decode('utf-8').encode(chartype)

def gredict(Dictionary, a):
    xs=dictfind(Dictionary, a)
    
    for x in xs:
        getDscp(Dictionary,x)

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

    Dictionary=dictload('dict.txt')

    if len(sys.argv)>1:
        for a in sys.argv[1:]:
            gredict(Dictionary,a)
    else:
        while 1:
            try:
                word=raw_input('Enter word to search: ')
                gredict(Dictionary,word)
            except:
                break
    print '\nBye'
    
if __name__=='__main__':
    main()
