class Dog:
  owner=True
  teeth=42
  happy_wagging_tail=True
  legs=4
  def __init__(self,name):
    self.name=name
  def bark(self):
    print("woof woof")
tommy=Dog("tommy")
maxi=Dog("maxi")
print(tommy.name)
print(maxi.name)
print(tommy.happy_wagging_tail)
print(maxi.happy_wagging_tail)
