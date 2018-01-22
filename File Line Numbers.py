#This program reads in a text file and returns the a new file with the same 
# content but with line numbers
file = input("Enter in a file you want to open and remake:")
rfile = open(file,"r")
wfile = open("New File.txt","w")
count = 0
for line in rfile:
    count = count + 1
    linee = str(count) + " " + line
    wfile.write(str(linee))
rfile.close()
wfile.close()
