#this program determines the highest profit from a sale of apples given
#a list of prices
def main():
    budget = 100
    prices = [14,6,9,7,8,10,3,9]
    x = 0
    y = 0
    for i in range(len(prices)):
        apples = 100/prices[i]
        if(i<7):
            money = (apples)*(prices[i+1])
            x = money
            if x > y:
                y = x
                b = prices[i]
                s = prices[i+1]
            print(money)
    print("The greatest profit is: " , y,", by buying at ",b,"$ and selling at",s,"$.")
main()
