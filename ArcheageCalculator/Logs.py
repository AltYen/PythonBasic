import datetime

def taketime(): #function for the take current time.
    time = datetime.datetime.now() #taking current timem
    a="{}/{}/{} | {}:{}".format(time.day, time.month, time.year, time.hour, time.minute)
    return a

def read(): #function for the read from txt.file
    log = open("log.txt", "r")
    print(log.read())

def write(text):#function for the write info to txt.file
    log=open("log.txt","a")
    log.write(text)