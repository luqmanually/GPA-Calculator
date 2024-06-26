class GPA:
    def __init__(self):
        self.grades = []
        self.worth = []
        self.unwgpa = 0
        self.wgpa = 0
        self.ctletter = []
        self.decision = None

    def GetData(self):
        for i in range(7):
            self.gradeletter = input("What grade do you have? (A,B,C etc.) \n")
            self.grades.append(self.gradeletter)
            self.validginput()
            self.classtype = input("Is it a regular, honors, or AP class? \n")
            self.worth.append(self.classtype)
            self.ctletter += self.worth[-1]
            self.validtinput()
        self.calculate()
        self.GorB()
        self.showweighted()

    def validginput(self):
        if self.grades[-1].lower() not in "abcdf":
            print("Please only use A, B, C, D, or F")
            self.gradeletter = input("What grade do you have? \n")
            self.grades[-1] = self.gradeletter
            self.validginput()
        else:
            pass

    def validtinput(self):
        if self.ctletter[0].lower() not in "rha":
            print("Please only use regular, honors, or AP")
            self.classtype = input("Is it a regular, honors, or AP? \n")
            self.worth[-1] = self.classtype
            self.ctletter = []
            self.ctletter += self.worth[-1]
            self.validtinput()
        else:
            self.ctletter = []

    def calculate(self):
        for i in self.grades:
            if i.lower() == "a":
                self.unwgpa += 4
            elif i.lower() == "b":
                self.unwgpa += 3
            elif i.lower() == "c":
                self.unwgpa += 2
            elif i.lower() == "d":
                self.unwgpa += 2
            else:
                self.unwgpa += 1
        self.wgpa = self.unwgpa
        self.unwgpa /= 7
        self.unwgpa = round(self.unwgpa, 3)

    def calcweighted(self):
        for i in self.worth:
            if i[0].lower() == "h":
                self.wgpa += .5
            elif i[0].lower() == "a":
                self.wgpa += 1
            else:
                continue
                # why wouldnt we use pass??
        self.wgpa /= 7
        self.wgpa = round(self.wgpa, 3)

    def GorB(self):
        if self.unwgpa > 3:
            print(f"Yay your Gpa is {self.unwgpa}, good job!")
        else:
            print(f"Yikes your Gpa is {self.unwgpa}....")

    def showweighted(self):
        self.decision = input("Would you like to see your weighted gpa? (Yes or No) \n")
        if self.decision == "yes":
            self.calcweighted()
            print(f"Your weighted gpa is {self.wgpa}")
        elif self.decision == "no":
            print("Okay have a good day :D")
        else:
            print("Please only type in Yes or No")
            self.showweighted()

print("Welcome to Hannahs GPA calculator!")
student = GPA()
student.GetData()
