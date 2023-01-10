
prime = [2]


for i in range(3,100):
    check = 0
    
    for j in range(len(prime)):
        
        if i % prime[j] == 0:
            check = 0
            break;
        
        else:
            check += 1;

    if check == len(prime):
        prime.append(i)


for k in prime:
    print(k , end = ", ")
        
            
