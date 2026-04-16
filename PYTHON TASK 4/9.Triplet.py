list=[10,20,30,9]
for i in range(len(list)):
    for j in range(i+1,len(list)):
        for k in range(j+1,len(list)):
            if list[i]+list[j]+list[k] ==59:
                print (list[i],list[j],list[k])