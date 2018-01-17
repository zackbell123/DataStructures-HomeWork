#This program reads in a file and outputs the file with the line number
def main():
    counter = 0
    infile = open("hw.py",'r')
    for line in infile.readLines():
        print(counter,line)
        counter = counter + 1
main()
    
