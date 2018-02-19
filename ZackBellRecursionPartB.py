#This program takes finds the nth fibonacci number
#Zack Bell
import time
memory = []
def fib(n):
    if(n<=1):
        return n
    else:
        return fib(n-1) + fib(n-2)
    
def fibo(n):
    x,y = 1,1
    for i in range(n-1):
        x,y = y,x+y
    return x
def fibod(n):
    x,y = 1,1
    if(len(memory)>=n):
        return memory[n]
    else:
        for i in range(n-1):
            x,y = y,x+y
        memory.append(x)
        return x
def main():
    x = 0
    while(x!=50):
        x = int(input("Enter in a number: "))
        tR1 = time.clock()
        print(fib(x))
        tR2 = time.clock()
        tL1 = time.clock()
        print(fibo(x))
        tL2 = time.clock()
        tD1 = time.clock()
        print(fibod(x))
        tD2 = time.clock()
        tRec = tR2 - tR1
        tDyn = tD2 - tD1
        tLoo = tL2 - tL1
        print("Recursive: ", tRec)
        print("Loop: ",tLoo)
        print("Dynamic: ",tDyn)
main()
