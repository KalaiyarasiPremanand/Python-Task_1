Numbers =[10,501,22,37,100,999,87,351]
even =[]
odd=[]
for n in Numbers: 
    if n % 2==0:
        even.append(n)
    else:
        odd.append(n)
print("even numbers:",even)
print("odd numbers:",odd)
