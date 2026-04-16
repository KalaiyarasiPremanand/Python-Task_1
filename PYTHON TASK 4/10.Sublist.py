list =[4,2,-3,1,6]
n = len(list)
for i in range(n):
    s=0
    for j in range(i,n):
        s += list[j]
        if s==0:
            print("sublist with sum 0 exists")
            break
       
