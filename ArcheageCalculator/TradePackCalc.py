import Logs

class TradePackCalc:
    def __init__(self):
        self.nuiapack = [["Solzreed Local Pack", "Meat", 180, "Grape", 30], # Some info about the packs in the game
                    ["Solzreed Specialty Pack", "Meat", 300, "Egg", 10],
                    ["Lilyut Hills Local Pack", "Dried Flowers", 180, "Olive", 3],
                    ["Lilyut Hills Specialty Pack", "Ground Spices", 300, "Milk", 5],
                    ["Dewstone Local Pack", "Narcissus", 180, "Medicinal Powder", 50],
                    ["Dewstone Specialty Pack", "Ground Grain", 300, "Wool", 10],
                    ["Marioneple Local Pack", "Ground Spices", 180, "Cherry", 2],
                    ["Marioneple Specialty Pack", "Dried Flowers", 300, "Duck Down", 10],
                    ["Two Crowns Local Pack", "Ground Grain", 180, "Pomegranate", 3],
                    ["Two Crown Specialty Pack", "Medicinal Powder", 300, "Milk", 5]]

        self.haranyapack = [["Mahadevi Local Pack", "Orchard Puree", 180, "Fig", 5], # Some info about the packs in the game
                         ["Mahadevi Specialty Pack", "Chopped Produce", 300, "Banana", 5],
                         ["Solis Local Pack", "Medicinal Powder", 180, "Jujube", 2],
                         ["Solis Specialty Pack", "Medicinal Powder", 300, "Yata Fur", 10],
                         ["Sunbite Local Pack", "Orchard Puree", 180, "Lavender", 15],
                         ["Sunbite Specialty Pack", "Medicinal Powder", 300, "Lemon", 15],
                         ["Arcum Iris Local Pack", "Dried Flowers", 180, "Turmeric", 3],
                         ["Arcum Iris Specialty Pack", "Ground Spices", 300, "Egg", 10],
                         ["Silent Forest Local Pack", "Ground Spices", 180, "Pomegranate", 3],
                         ["Silent Forest Specialty Pack", "Orchard Puree", 300, "Milk", 5]]


    def PackCalc(self,nation): #calculating function

        if nation=="Nuia":

            print()
            for i in range(len(self.nuiapack)): # listing "Nuia" packs to show user
                print("%d. %s" % (i + 1, self.nuiapack[i][0]))

            choice = int(input("\nWhich one do you want to do : ")) #taking choice
            amount = int(input("How many %s do you want to craft :" % (self.nuiapack[choice - 1][0]))) #taking amount

            Logs.write(" Calculation was made for {} {} - [{}]\n".format(amount, self.nuiapack[choice - 1][0], Logs.taketime())) #saving log to txt file

            return "\nYou need {0} {1} - {2} {3} \nTo craft {4} {5} ".format((self.nuiapack[choice - 1][2] * amount),self.nuiapack[choice - 1][1], (self.nuiapack[choice - 1][4] * amount), self.nuiapack[choice - 1][3], amount,self.nuiapack[choice - 1][0]) #return the result

        if nation=="Haranya":

            print()
            for i in range(len(self.haranyapack)): # listing "Haranya" packs to show user
                print("%d. %s" % (i + 1, self.haranyapack[i][0]))

            choice = int(input("\nWhich one do you want to do : ")) #taking choice
            amount = int(input("How many %s do you want to craft :" % (self.haranyapack[choice - 1][0]))) #taking amount

            Logs.write("Calculation was made for {} {} - [{}]\n".format(amount, self.haranyapack[choice - 1][0], Logs.taketime())) #saving log the txt file

            return "\nYou need {0} {1} - {2} {3} \nTo craft {4} {5} ".format((self.haranyapack[choice - 1][2] * amount), self.haranyapack[choice - 1][1],(self.haranyapack[choice - 1][4] * amount), self.haranyapack[choice - 1][3], amount, self.haranyapack[choice - 1][0]) #return the result

