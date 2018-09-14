# Netology, assignment 5 

class Animal:
  name = None
  color = None
  weight = 0
  fed = False
  voice = 'Hmm...'
  subclass = 'Mammal'
  tame = 'Domestic'
  animals = {}
  
  def __init__(self, name, color, weight):
    self.name = name
    self.color = color
    self.weight = weight
    self.animals[self.name] = self.weight
  
  def feed(self):
    self.fed = True
    print('{} is now fed.'.format(self.name))
  
  def speak(self):
    print('{} says: {}'.format(self.name, self.voice))
    
class Mammal(Animal):
  milked = False
  
  def milk(self):
    self.milked = True
    print('{} is now milked.'.format(self.name))
  
class Bird(Animal):
  subclass = 'Bird'
  eggs = False
  
  def collect_eggs(self):
    self.eggs = True
    print('Eggs are collected from {}.'.format(self.name))
    
class Goose(Bird):
  voice = "Honk-honk"
  
class Duck(Bird):
  voice = 'Quack-quack'
  
class Chicken(Bird):
  voice = 'Cluck-cluck'
  
class Cow(Mammal):
  voice = 'Moo-moo'

class Sheep(Mammal):
  voice = 'Baa-baa'
  fleeced = False
  
  def fleece(self):
    self.fleeced = True
    print('{} is now fleeced.'.format(self.name))
  
class Goat(Mammal):
  voice = 'Maa-maa'
  fleeced = False
  
  def fleece(self):
    self.fleeced = True
    print('{} is now fleeced.'.format(self.name))
    
goose_1 = Goose('Grey', 'grey', 3)
goose_2 = Goose('White', 'white', 4)
chicken_1 = Chicken('Co-Co', 'white', 2)
chicken_2 = Chicken('Coo-Ka-Re-Coo', 'brownish', 3)
duck_1 = Duck('Quryackwa', 'grey', 2)
cow_1 = Cow('Manka', 'brown', 450)
sheep_1 = Sheep('Barashek', 'milky', 100)
sheep_2 = Sheep('Quodryawy', 'milky', 87)
goat_1 = Goat('Horn', 'black', 64)
goat_2 = Goat('Hoof', 'grey', 77)

goose_1.feed()
goose_1.speak()
goose_1.collect_eggs()

goose_2.feed()
goose_2.speak()
goose_2.collect_eggs() 

chicken_1.feed()
chicken_1.speak()
chicken_1.collect_eggs() 

chicken_2.feed()
chicken_2.speak()
chicken_2.collect_eggs() 

duck_1.feed()
duck_1.speak()
duck_1.collect_eggs()

cow_1.feed()
cow_1.speak()
cow_1.milk()

sheep_1.feed()
sheep_1.speak()
sheep_1.milk()
sheep_1.fleece()

sheep_2.feed()
sheep_2.speak()
sheep_2.milk()
sheep_2.fleece()

goat_1.feed()
goat_1.speak()
goat_1.milk()
goat_1.fleece()

goat_2.feed()
goat_2.speak()
goat_2.milk()
goat_2.fleece()

sum_weight = 0
max_weight = 0
winner = None
for weight in Animal.animals.values():
  sum_weight += weight

for name, weight in Animal.animals.items():
  if weight > max_weight:
    max_weight = weight
    winner = name
print('Total weight of all farm animals: {}'.format(sum_weight))
print('The heaviest animal on the farm is {}'.format(winner))
