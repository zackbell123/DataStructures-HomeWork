#This program runs although I wasn't able to A. Print out the patients, and
# B. Fully create the flow of the patients.
#I worked on some of this code with Roger Robinson and in class
import random
names = ["joe", "bobby", "suesan", "loretta", "grant", \
         "jenny", "billy", "tucker", "cletus", "hunter", \
         "gunner", "rose", "amy", "charlotte", "duke", \
         "ricky", "bo", "duke", "jesse", "bubba"]
waitingRoom = []
triageRoom = []
examRoom = []
examRoomSize = 6
doctors = 6
def callNurse():
    """move patient from waiting room to triage room"""
    triageRoom.append(waitingRoom.pop(0))
class Patient():
    time = 0
    def __init__(self, time):
        ran1 = random.randint(0,(len(names)-1))
        ran2 = random.randint(0,len(names)) 
        self.triageNumber = random.randint(0,100)
        self.name = names[ran1] \
        + names[ran2-1]
        self.arrivalTime = time
        self.treatmentTime = random.randrange(15, 20)
    def exit(self):
        examRoom.pop(0)
    def getEntryTime(time):
        self.entryTime = time
        return self.entryTime
    def getExitTime(time):
        self.exitTime = time
        return self.exitTime
def sim():
    pats = int(input("Enter in the number of patients there will be: "))
    time = 0
    x = 0
    for i in range(pats):
        pats-=1
        p = Patient(time)
        waitingRoom.append(p)
    while x == 0:
        for i in range(len(waitingRoom)):
            callNurse()
        for p in triageRoom:
            if(len(examRoom)<6):
                examRoom.append(p)
        for p in examRoom:
            p.treatmentTime - 1
            print(p.treatmentTime)
            if p.treatmentTime == 0:
                examRoom.remove(0)
            if len(examRoom) == 0:
                x = 1
        time+=1
sim()
    
        
                
    
    
        
                                  

