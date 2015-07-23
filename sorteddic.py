import os,sys

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
    
def main():
    ifs=['\xc2\xa0','\xef\x80\xa0']

    mydict=dictload('gre3000.dict')
    sdict=[]
    
    for k,v in mydict.items():
        for i in ifs:
            k=k.replace(i,'')
        sdict.append((len(k.strip()),k.strip(),v))
    sdict=sorted(sdict)
    
    chartype = sys.getfilesystemencoding()    
    
    for s in sdict:
        print s[0],'|'+s[1].decode('utf-8').encode(chartype)+'|\t'+s[2].decode('utf-8').encode(chartype),

if __name__=='__main__':
    main()
