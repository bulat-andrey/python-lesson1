class Dog:
	def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def bark(self):
        print("bark bark!")
        
    def doginfo(self):
        print(self.name + " is " + str(self.age) + " year(s) old.")