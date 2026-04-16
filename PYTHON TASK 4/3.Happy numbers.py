numbers = [10,501,22,37,100,999,87,351]
count=0
for n in numbers:
    while n!= 1 and n!= 4:
        n = sum(int(d)**2 for d in str (n))
    if n==1:
        count +=1
print(count)
