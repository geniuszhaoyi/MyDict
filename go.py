f=open('words.a.txt').read()



x=f.split()
open('reading36.w.txt','w').write(f)
words={}
for I in x:
    i=I.lower()
    if i not in words: words[i]=0
    words[i]+=1

fw=open('reading36.l.txt','w')

for k,v in words.items():
    fw.write(str(v)+'\t'+k+'\n')

fw.close()

