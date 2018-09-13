class Car:
    def _init_(self,name,color):
        self.name=name
        self.color=color
        self.speed=0
    def increasespeed(self):
        self1.speed +=10
        print(self.speed)
    def _str_(self):
        return ("my name is" + self.name + ",color:"+self.color)
car=Car("M","Red")
car.increasespeed()
print(car)
