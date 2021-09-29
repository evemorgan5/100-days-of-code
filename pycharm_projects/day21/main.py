# chef
# methods
# bake()
# stir()
# measure()

# create pastry chef

# bake()
# stir()
# measure()
# knead()
# whisk()

# class inheritance
# appearance & behavior

class Animal:
    def __init__(self):
       self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal):
    def __init__(self):
        super().__init__()
    #     allows it to inherit any thing from super class which is animal calss

    def breathe(self):
        super().breathe()
        print("doing this underwater.")


    def swim(self):
        print("moving in water.")


nemo = Fish()
# nemo.swim()
nemo.breathe()
# print(nemo.num_eyes)

