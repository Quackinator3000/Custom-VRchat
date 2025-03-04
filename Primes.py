# Print all prime numbers from 1 - 1,000,000

primes = [1, 2, 3]
i = 4
check = 2
c = 0

while i < 1000001:
    check = 2
    while check < i + 1: # Continue while in range
        
        if i == check:
            print(f"Prime number found!: {i}")
            c = c + 1
            primes.append(i)
            i = i + 1
            break
        elif i % check == 0:
            i = i + 1
            break            
        else:
            check = check + 1 

print(f"Number of primes found: {c} :exiting now...")       