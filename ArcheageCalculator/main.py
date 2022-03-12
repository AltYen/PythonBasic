import TimeCalc
import TradePackCalc
import FarmCalc
import Logs
import time

#I made this program for the benefit of myself and my guild friends in the game called "Archeage".
# In short, I did it to make some calculations in the game easily.
# For example, the nearest event time, Showing the current location of the Cargo ship in the game,
# Calculating the amount of materials required for the trade packages to earn money,
# Calculating how much we will collect from some of the things we plant in our garden.
# So far I have been able to do this. There is so much more I can add.


eventtimecalc=TimeCalc.EventTimeCalc() #creating object from EventTimeCalc class from TimeCalc.py
cargoshipcalc=TimeCalc.CargoShipCalc() #creating object from CargoShipCalc class from TimeCalc.py
tradepackcalc=TradePackCalc.TradePackCalc() #creating object from TradePackCalc class from TradePackCalc.py
farmpackcalc=FarmCalc.FarmCalculator() #creating object from FarmCalculator class from FarmCalc.py

while True: #The structure that allows the program to run until the user enters 6 as an input.
    print("""
    1.Event Time Check
    2.Cargo Ship Status
    3.Trade Pack Calculator
    4.Farm Calculator
    5.Log
    6.Quit
    """)
    while True: # try-except loop with while until user enters true value
        try:
            choice=int(input("Enter your Choice : "))
            if(choice>=1 and choice<=6):
                break
        except:
            print("pls enter only number with 1 and 6")

    if choice==1:
        Logs.write("The 1th option is selected in the main menu.- [{}]\n".format(Logs.taketime())) #We save the process to the txt file with the write function from logs.py.
        leftcrtime=eventtimecalc.CrRemainingTime() #using the object we created.
        leftgrtime=eventtimecalc.GrRemainingTime() #using the object we created.

        print()
        print(leftcrtime)
        print(leftgrtime,"\n")

        time.sleep(5) #We add delay so that the user can read the result.

    if choice==2:
        Logs.write("The 2nd option is selected in the main menu.- [{}]\n".format(Logs.taketime())) #We save the process to the txt file with the write function from logs.py.
        cargostatus=cargoshipcalc.Where() #using the object we created.
        print()
        print(cargostatus)

        time.sleep(5) #We add delay so that the user can read the result.

    if choice==3:
        Logs.write("The 3rd option is selected in the main menu.- [{}]\n".format(Logs.taketime())) #We save the process to the txt file with the write function from logs.py.

        while True: # try-except loop with while until user enters true value
            try:
                nation=input("Which Nation (Nuia | Haranya): ")
                if(nation=="Nuia" or nation=="Haranya"):
                    break
            except:
                print("pls enter the string value")

        print(tradepackcalc.PackCalc(nation)) #using the object with sending some value to function we created.
        time.sleep(5) #We add delay so that the user can read the result.

    if choice==4:
        Logs.write("The 4th option is selected in the main menu.- [{}]\n".format(Logs.taketime())) #We save the process to the txt file with the write function from logs.py.
        print("""
        1.Seed
        2.Saplins
        3.Livestock""")

        print()
        while True: # try-except loop with while until user enters true value
            try:
                choice = int(input("Choice : "))
                if (choice >= 1 and choice <= 3):
                    break
            except:
                print("pls enter only number with 1 and 3")

        if(choice==1):
            farmpackcalc.SeedCalc()#using the object we created.
        if (choice == 2):
            farmpackcalc.SaplingCalc()#using the object we created.
        if (choice == 3):
            farmpackcalc.LiveStockCalc()#using the object we created.

        time.sleep(5) #We add delay so that the user can read the result.

    if choice==5:
       Logs.write("The 5th option is selected in the main menu. - [{}]\n".format(Logs.taketime())) #We save the process to the txt file with the write function from logs.py.
       print()
       Logs.read() # reading txt file
       time.sleep(5) #We add delay so that the user can read the result.

    if choice==6:
        Logs.write("Quit - [{}]\n".format(Logs.taketime())) #We save the process to the txt file with the write function from logs.py.
        break








