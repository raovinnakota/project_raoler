def sum_multiple(number, factors):
    sum = 0
    
    for i in range(number):
        for j in factors:
            if (i % j == 0):
                sum = sum + i
                break
    return(sum)

def brute_force():
    sum = 0
    
    for i in range(1000):
        if ((i % 3 == 0) or (i % 5 == 0)):
            sum = sum + i
    return(sum)

print(brute_force())
print(sum_multiple(1000, [3, 5]))