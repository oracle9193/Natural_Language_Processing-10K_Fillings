import os

for k in range (1,262):
    f=file("C:/research/HIT_QIWEI/data/twosection0504/clean_"+str(k)+".txt")
    i=0
    for line in f:
        i+=1
        if '++++' in line:
            break
    print i
    f.close()

    f1=file("C:/research/HIT_QIWEI/data/twosection0504/clean_"+str(k)+".txt")
    lines1=[]
    lines2=[]
    j=0
    for line in f1:
       j=j+1
       if j<=i:
           lines1.append(line)
       else:
           lines2.append(line)

    outfile1= file("C:/research/HIT_QIWEI/data/clean/business/"+str(k)+".txt","w")
    outfile1.writelines(lines1)

    outfile2= file("C:/research/HIT_QIWEI/data/clean/risk/"+str(k)+".txt","w")
    outfile2.writelines(lines2)

    outfile1.close()
    outfile2.close()



