import Logs

class FarmCalculator:

    def __init__(self):
        self.seeds = ["Rose", 2, 4, 2], ["Azalea", 2, 4, 3], ["Rice", 3, 5, 3], ["Barley", 2, 6, 3], ["Potato", 2, 7, 1], ["Garlic", 2, 5, 4], ["Mushroom", 3, 7, 1] #some info about seeds from the game
        self.saplings = ["Cedar", 8, 10, 18], ["Aspen", 8, 14, 30], ["Oak", 4, 6, 14], ["Lemon", 5, 10, 24], ["Banana", 5,10, 24], ["Cork", 6, 8, 15], ["Apple", 5, 10, 24] #some info about the sapligs from the game
        self.livestock = ["Pig", "Meat", 15, 20, "Leather", 18, 22, 10], ["Duckling", "Duck Down", 5, 8, 4], ["Lamb", "Wool",15, 19, 10], ["Cow", "Milk", 10, 15, 21], ["Turkey Chick", "Meat", 4, 8, "Leather", 3, 5, 3], ["Chick", "Egg",3, 5, 2], ["Gosling", "Goose Down", 4, 8, 4] #some info about the livestocks from the game

    def SeedCalc(self): #calculation function for the seeds
        print()
        for i in range(len(self.seeds)): # listing all seeds to show user
            print("%d. %s" % (i + 1, self.seeds[i][0]))

        print()
        while True: # try-except loop with while until user enters true value
            try:
                choice = int(input("Choice : "))
                if (choice >= 1 and choice <= 7):
                    amount = int(input("How many will u plant? :"))
                    break
            except:
                print("pls enter the integer value")

        Logs.write("Calculation was made for {} {} - [{}]\n".format(amount,self.seeds[choice-1][0],Logs.taketime())) #saving log to txt file
        print()

        print("In the most unlucky situation you will get {0} {1} in {2}h".format(self.seeds[choice - 1][1] * amount,self.seeds[choice - 1][0],self.seeds[choice - 1][3]))
        print("In average lucky situation you will get {0} {1} in {2}h".format((self.seeds[choice - 1][1] * amount + self.seeds[choice - 1][2] * amount) / 2, self.seeds[choice - 1][0],self.seeds[choice - 1][3]))
        print("In the most lucky situation you will get {0} {1} in {2}h".format(self.seeds[choice - 1][2] * amount,self.seeds[choice - 1][0],self.seeds[choice - 1][3]))

    def SaplingCalc(self): #calculation function for the saplings
        print()
        for i in range(len(self.saplings)): # listing saplings to show user
            print("%d. %s" % (i + 1, self.saplings[i][0]))


        print()
        while True:  # try-except loop with while until user enters true value
            try:
                choice = int(input("Choice : "))
                if (choice >= 1 and choice <= 7):
                    amount = int(input("How many will u plant? :"))
                    break
            except:
                print("pls enter the integer value")

        Logs.write("Calculation was made for {} {} - [{}]\n".format(amount, self.saplings[choice - 1][0], Logs.taketime())) #saving log to txt file

        print()
        print("In the most unlucky situation you will get {0} {1} in {2}h".format(self.saplings[choice - 1][1] * amount,self.saplings[choice - 1][0],self.saplings[choice - 1][3]))
        print("In average lucky situation you will get {0} {1} in {2}h".format((self.saplings[choice - 1][1] * amount + self.saplings[choice - 1][2] * amount) / 2, self.saplings[choice - 1][0],self.saplings[choice - 1][3]))
        print("In the most lucky situation you will get {0} {1} in {2}h".format(self.saplings[choice - 1][2] * amount,self.saplings[choice - 1][0],self.saplings[choice - 1][3]))

    def LiveStockCalc(self): #calculation function for the livestocks
        print()
        for i in range(len(self.livestock)): # listing livestocks to show user
            print("%d. %s" % (i + 1, self.livestock[i][0]))

        print()
        while True:  # try-except loop with while until user enters true value
            try:
                choice = int(input("Choice : "))
                if (choice >= 1 and choice <= 7):
                    amount = int(input("How many will u plant? :"))
                    break
            except:
                print("pls enter the integer value")

        Logs.write("Calculation was made for {} {} - [{}]\n".format(amount, self.livestock[choice - 1][0], Logs.taketime())) #saving log to txt file

        control = len(self.livestock[choice - 1])
        print()
        if (control == 8): #The fugitive solution I found due to the difference in the number of elements in the arrays

            print("In the most unlucky situation you will get {0} {1} in {2}h and {3} {4} in {5}h".format(
                self.livestock[choice - 1][2] * amount, self.livestock[choice - 1][1], self.livestock[choice - 1][7],
                self.livestock[choice - 1][5] * amount, self.livestock[choice - 1][4], self.livestock[choice - 1][7]))
            print("In average lucky situation you will get {0} {1} in {2}h and {3} {4} in {5}h".format(
                (self.livestock[choice - 1][2] * amount + self.livestock[choice - 1][3] * amount) / 2, self.livestock[choice - 1][1],
                self.livestock[choice - 1][7], (self.livestock[choice - 1][5] * amount + self.livestock[choice - 1][6] * amount) / 2,
                self.livestock[choice - 1][4], self.livestock[choice - 1][7]))
            print("In the most lucky situation you will get {0} {1} in {2}h and {3} {4} in {5}h".format(
                self.livestock[choice - 1][3] * amount, self.livestock[choice - 1][1], self.livestock[choice - 1][7],
                self.livestock[choice - 1][6] * amount, self.livestock[choice - 1][4], self.livestock[choice - 1][7]))

        else:
            print("In the most unlucky situation you will get {0} {1} in {2}h".format(self.livestock[choice - 1][2] * amount,self.livestock[choice - 1][1],self.livestock[choice - 1][4]))
            print("In average lucky situation you will get {0} {1} in {2}h".format((self.livestock[choice - 1][2] * amount + self.livestock[choice - 1][3] * amount) / 2, self.livestock[choice - 1][1],self.livestock[choice - 1][4]))
            print("In the most lucky situation you will get {0} {1} in {2}h".format(self.livestock[choice - 1][3] * amount,self.livestock[choice - 1][1],self.livestock[choice - 1][4]))
