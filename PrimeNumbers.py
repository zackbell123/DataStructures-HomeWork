#Goes through numbers 1 to 50 to find prime numbers
def main():
    for i in range(2,50):
        isPrime = True
        for j in range(2,i):
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            print(i)
main()
    
        
    
