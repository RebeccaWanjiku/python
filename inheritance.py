class Dad:
            def football(self):
                    print("Dad likes watching football")

class Mom:
            def cooking(self):
                print("Mom likes cooking")

class Boy(Dad):
    def boyage(self):
        print("I'm 20 years old")

my_boy=Boy
my_boy.football()
my_boy.boyage()

class Girl(Mom):
    def makeup(self):
        print("I love gloss")

my_girl=Girl
my_girl.makeup()
my_girl.cooking()