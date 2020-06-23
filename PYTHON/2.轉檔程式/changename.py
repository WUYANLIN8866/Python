import os
import time
nowtime = time.asctime( time.localtime(time.time()) )
Filelocation=input('Please enter the file path location(End with \)：')
Changename=input('Please enter a change name:') 
Deputyfilename=input('Please enter the change deputy file name(example:.txt):') 
f=os.listdir(Filelocation)
n=0
for i in f:
    name1=Filelocation+f[n]
    name2=Filelocation+Changename+str(n+1)
    os.rename(name1,name2)
    print(name1,'is changed name',name2,Deputyfilename,'at',nowtime)
    n+=1