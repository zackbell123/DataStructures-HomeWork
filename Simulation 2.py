
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
    def examTime(self):
        self.treatmentTime-=1
    def exit(self):
        examRoom.pop(0)
    def getEntryTime(self,time):
        self.entryTime = time
        return self.entryTime
    def getExitTime(self,time):
        self.exitTime = time
        return self.exitTime
def sim():
    time = 0
    y = 1
    pats = int(input("Enter in the number of patients there will be: "))
    x = 0
    for i in range(pats):
        p = Patient(time)
        waitingRoom.append(p)
    for p in waitingRoom:
        callNurse()
        print(p.name)
        time+=1
    while x == 0:
        for p in triageRoom:
            triageRoom.remove(p)
            if(len(examRoom)<6):
                examRoom.append(p)
        for p in examRoom:
            p.examTime()
            if p.treatmentTime == 0:
                examRoom.remove(p)
                print(p.name, (time - p.treatmentTime))
            if len(examRoom) == 0:
                x = 1
        time+=1
sim()
    
        
                
    
    
        
                                  

