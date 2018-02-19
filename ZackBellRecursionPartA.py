#This program takes a number and finds the times it takes to reach 1 using
#the Collatz Conjecture
def col(num,times):
    if(num==1):
        return times
    elif(num%2==0):
        times = times + 1
        return col(num/2,times)
    else:
        times = times + 1
        return col((3*num)+1,times)
def main():
    x = int(input("Enter in a positive integer: "))
    print(col(x,0))
main()
    

        
        
