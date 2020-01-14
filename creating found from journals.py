import csv
jcl=[]
sjrl=[]
hil=[]
td17l=[]
td3l=[]
trl=[]
tcl=[]
cd3l=[]
cd2l=[]
rdl=[]



with open("journals.csv",'r') as csvfile:
    c = csv.reader(csvfile)
    for r in c:
        for i in range(1,len(r)):
            r[0]+=r[i]
            
        k=r[0].find('"')
        l=r[0].find('"',k+1)
        jour=r[0][k+1:l]
        
        k=l+1
        l=r[0].find(';',k+1)
        k=l
        l=r[0].find(';',k+1)

        k=l
        l=r[0].find(';',k+1)
        x=r[0][k+1:l]
        try:
            x=int(x)
        except:
            x=-1
        x/=1000
        sjrl.append(x)

        k=l
        l=r[0].find(';',k+1)
        k=l
        l=r[0].find(';',k+1)
        x=r[0][k+1:l]
        try:
            x=int(x)
        except:
            x=-1
        hil.append(x)
        
        k=l
        l=r[0].find(';',k+1)
        x=r[0][k+1:l]
        try:
            x=int(x)
        except:
            x=-1
        td17l.append(x)
        
        k=l
        l=r[0].find(';',k+1)
        x=r[0][k+1:l]
        try:
            x=int(x)
        except:
            x=-1
        td3l.append(x)

        k=l
        l=r[0].find(';',k+1)
        x=r[0][k+1:l]
        try:
            x=int(x)
        except:
            x=-1
        trl.append(x)

        k=l
        l=r[0].find(';',k+1)
        x=r[0][k+1:l]
        try:
            x=int(x)
        except:
            x=-1
        tcl.append(x)

        k=l
        l=r[0].find(';',k+1)
        x=r[0][k+1:l]
        try:
            x=int(x)
        except:
            x=-1
        cd3l.append(x)

        k=l
        l=r[0].find(';',k+1)
        x=r[0][k+1:l]
        try:
            x=int(x)
        except:
            x=-1
        x/=100
        cd2l.append(x)

        k=l
        l=r[0].find(';',k+1)
        x=r[0][k+1:l]
        try:
            x=int(x)
        except:
            x=-1
        x/=100
        rdl.append(x)
        
        jcl.append(jour)
        
jcl=jcl[1:]
sjrl=sjrl[1:]
hil=hil[1:]
td17l=td17l[1:]
td3l=td3l[1:]
trl=trl[1:]
tcl=tcl[1:]
cd3l=cd3l[1:]
cd2l=cd2l[1:]
rdl=rdl[1:]

jtl=[]
il=[]
file = open('journals.txt','r')
l=file.readlines()
for r in l:
    j=r.find(';')
    k=r.find(';',j+1)
    jtl.append(r[j+1:k])
    il.append(r[k+1:])

file = open("found.txt",'w')
for i in range(len(jcl)):
    for j in range(len(jtl)):
        if jcl[i].lower()==jtl[j].lower():
            file.write(jcl[i]+";"+str(sjrl[i])+";"+str(hil[i])+";"+str(td17l[i])+";"+str(td3l[i])+";"+str(trl[i])+";"+str(tcl[i])+";"+str(cd3l[i])+";"+str(cd2l[i])+";"+str(rdl[i])+";"+str(il[j]))
            break

            
    
    
    
    
    
    
    

    
    
