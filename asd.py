#coding:utf-8

import re

key=re.compile(r'^[\S]+')

f=open('gre3000.dict')
ls=f.readlines()
fw=open('asd.sql','w')

for l in ls:
    #print l
    x=re.match(key,l).group().replace(" ",'').strip()
    y=l.replace(x,'',1).replace(" ",'').strip().replace("'","''")
    ss="UPDATE `WordBase` set `desc`='"+y+"' WHERE `word`='"+x+"' ;"
    fw.write(ss+'\n')

fw.close()
