class Result:

    def passed(self):

        with open("./testpassed.txt") as file:
            for line in file:
                print(line.replace("\n", " "))
            print("\n")

    def notpassed(self):
        with open("./testfailed.txt") as file:
            for line in file:
                print(line.replace("\n", " "))
            print("\n")

    def success(self):
        self.passed()
        with open("./surprised_pikachu.txt") as file:
            for line in file:
                print(line.replace("\n", " "))
            for i in range(3):
                print("\n")

    def failure(self):
        self.notpassed()
        with open("./guillotine.txt") as file:
            for line in file:
                print(line.replace("\n", " "))
            for i in range(3):
                print("\n")