class fruits :
    def __init__(self , name,color,price):
                            self.name=name
                            self.color=color
                            self.price=price
    def fruits(self):
        print(f"It's healthy to eat{self.name}."
                    f"It's  colour is {self.color}."
                     f"It costs {self.price}"
              )
myobj=fruits("Pineapple","yellow","Ksh 200")
myobj.fruits()
myobj=fruits("Apple","red","Ksh 50")
myobj.fruits()
myobj=fruits("Watermellon","green","Ksh 500")
myobj.fruits()
myobj=fruits("Blueberrys","Blue","Ksh 50")
myobj.fruits()
myobj=fruits("Dragon fruit","Pink","Ksh 550")
myobj.fruits()

