import numpy  as  np
import matplotlib.pyplot as plt
a=list(open('customer-file.csv'))
b=np.asarray(a)
c=np.array([])
for x  in b:
  c=np.append(c,x.split(','))

print(c.size)
name=list(c[0:3284:2])
num=list(c[1:3284:2])
q=0
vod=list()
idea=list()
ari=list()
jio=list()
comp=[vod,idea,ari,jio]
aseries=["7678","7710","7715","7716","7717","7718","7738","8450","8451","8452","8454","9004","9867","9892","9967","9987"]
vseries=["8879","9167","9619","9769","9930","9920","9833","9820","9820","9819","7506"]
jseries=["7021","7013","7002","6002","7004","7011","7000","7015","7018","7006","7019","7012","7003","7003","7016","7005","7008","7009","7014","6001","7010","6003","7017","7007","7001"]
iseries=["8108","8652","9594","9702","8419","8422","8424","8425","8689","8691","8692","8693"]
series=[vseries,iseries,aseries,jseries]
for  y  in num:
 for s in series:
    for k in s:
     for n in range(0,4):
       if s==series[n]:
         vod1 =  k in y
         if  vod1==True:
           comp[n].append(q)
 q+=1
clabel='vodafone','idea','ari','jio','other'
percet=(len(vod),len(idea),len(ari),len(jio),1642-len(vod)+len(idea)+len(ari)+len(jio))
color=("red","yellow","brown","blue","cyan")
plt.pie(percet,colors=color,labels=clabel,autopct='%1.2f',startangle=90)
plt.axis('equal')
plt.show()


























