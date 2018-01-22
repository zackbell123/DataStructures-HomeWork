#This program plays the game Fizzbuzz
def main():
    for i in range(1,100):
        word = ""
        if(i%3==0):
            word+="Fizz"
        if(i%5==0):
            word+="Buzz"
        if(word==""):
            word = i
        print(word)
main()
