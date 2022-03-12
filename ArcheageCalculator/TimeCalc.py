from datetime import timedelta
import datetime
import Logs


class CargoShipCalc:

    def __init__(self):
        self.nuiadock = [[0, 30], [2,00], [3, 30], [5, 00], [6, 30], [8, 00], [10, 30], [12, 00], [13, 30], [15, 00], [16, 30],[18, 00],[19, 30], [21, 00],[22, 30]] #some time info about the ship location
        self.haranyadock = [[1, 00], [2, 30], [4, 00], [5, 30], [7, 00], [8, 30], [10, 00], [11, 30], [13, 00], [14, 30], [16, 00],[17, 30],[19, 00], [20, 30],[22, 00],[23,30]] #some info about the ship location
        self.now = datetime.datetime.now() #taking current time.

    def Where(self): #calculator function

        for i in range(len(self.nuiadock)): #for loop to find nearest time
            takingtime = timedelta(hours=self.nuiadock[i][0], minutes=self.nuiadock[i][1]) #taking hour and munite from nuiadock by one by for the compare and find to nearist time
            currenttime = timedelta(hours=self.now.hour, minutes=self.now.minute) #taking only hour and munite from Current time
            if (self.nuiadock[i][0] > self.now.hour): #compare current time and taken time value from list
               reaminingtime1=takingtime-currenttime #taking diffrence beetwen current time and nearist time
               break

        for i in range(len(self.haranyadock)): #for loop to find nearest time
            takingtime = timedelta(hours=self.haranyadock[i][0], minutes=self.haranyadock[i][1]) #taking hour and munite from nuiadock by one by for the compare and find to nearist time
            currenttime = timedelta(hours=self.now.hour, minutes=self.now.minute) #taking only hour and munite from Current time
            if (self.haranyadock[i][0] > self.now.hour): #compare current time and taken time value from list
               reaminingtime2=takingtime-currenttime #taking diffrence beetwen current time and nearist time
               break

        Logs.write("Calculation was made for Cargo Ship Status[{}]\n".format(Logs.taketime())) #saving log to txt file

        if reaminingtime1<reaminingtime2: #comparing calculated 2 time because find to current ship location
            if((reaminingtime1.seconds/60)>30): #checking more value to find exactly location of ship
                return ("""
                Docked at Haranya Dock.
                %s left for coming Nuia Dock"""%str(reaminingtime1))
            else:
                return ("""
                Sailing to Nuia Dock.
                %s left for coming Nuia Dock"""%str(reaminingtime1))

        else:
            if ((reaminingtime2.seconds / 60) > 30): #checking more value to find exactly location of ship
                return ("""
                Docked at Nuia Dock.
                %s left for coming Haranya Dock""" % str(reaminingtime2))
            else:
                return ("""S
                ailing to Haranya Dock.
                %s left for coming Haranya Dock""" % str(reaminingtime2))




class EventTimeCalc:

    def __init__(self):
        self.crtime = [[0, 00], [2, 00], [4, 00], [6, 00], [8, 00], [10, 00], [12, 00], [14, 00], [16, 00], [18, 00], [20, 00],[22, 00]]#some time info about the cr event
        self.grtime = [[1, 00], [3, 00], [5, 00], [7, 00], [9, 00], [11, 00], [13, 00], [15, 00], [17, 00], [19, 00], [21, 00],[23, 00]]#some time info about the gr event
        self.now = datetime.datetime.now()  # taking current time.

    def CrRemainingTime(self): #calculator function

        for i in range(len(self.crtime)): #for loop to find nearest time
            takingtime = timedelta(hours=self.crtime[i][0], minutes=self.crtime[i][1])#taking hour and munite from crtime by one by for the compare and find to nearist time
            currenttime = timedelta(hours=self.now.hour, minutes=self.now.minute) #taking only hour and munite from Current time
            if (self.crtime[i][0] > self.now.hour): #compare current time and taken time value from list to calculate nearist event time
               reaminingtimecr=takingtime-currenttime #taking diffrence beetwen current time and nearist time
               break
        Logs.write("Calculation was made for Remaining Crimson Rift Event Time[{}]\n".format(Logs.taketime())) #saving log to txt file
        return ("Crimson Rift Event %s hours later"%str(reaminingtimecr)) #return the result

    def GrRemainingTime(self):
        for i in range(len(self.grtime)): #for loop to find nearest time
            takingtime = timedelta(hours=self.grtime[i][0], minutes=self.grtime[i][1]) #taking hour and munite from grtime by one by for the compare and find to nearist time
            currenttime = timedelta(hours=self.now.hour, minutes=self.now.minute) #taking only hour and munite from Current time
            if (self.grtime[i][0] > self.now.hour):#compare current time and taken time value from list to calculate nearist event time
               reaminingtimegr=takingtime-currenttime #taking diffrence beetwen current time and nearist time
               break

        Logs.write("Calculation was made for Remaining Grimghast Rift Event Time[{}]\n".format(Logs.taketime())) #saving log to txt file
        return ("Grimghast Rift Event %s hours later"%str(reaminingtimegr)) #return the result
