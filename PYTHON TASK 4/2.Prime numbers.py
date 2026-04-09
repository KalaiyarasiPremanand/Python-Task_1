Numbers = [10,501,22,37,100,999,86,351]
for n in Numbers:
    if n > 1 and all(n% i !=0 for i in range(2,n)):
        print (n,"is prime")


        
    