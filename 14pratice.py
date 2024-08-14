#nested class
class clothes:
    def __init__(self,colour):
        self.colour = colour

class model:
    def jeans(self):
        print("model jeans")

clothes_iteam = clothes("black")
model = model()
model.jeans()


#single inheritance

class Electronicedvice:
    def __init__(self, brand):
        self.brand = brand

    def switch_on(self):
     print("device switch on")

class mobile(Electronicedvice):
    def ring_call(self):
        print("ring  a call")  

class TV(Electronicedvice):
    def change_channel(self):
      print("changing channel")

phone = mobile("apple") 
tv = TV("MI")

phone.switch_on()
phone.ring_call()

tv.switch_on()
tv.change_channel()



#multilevel    


class Document:
    def __init__(self, title):
        self.title = title

    def whitespace(self) : 
        print(f"give white space:  {self.title}")

class TextDocument(Document): 
    def __init__(self, title, content):
        self.title = title
        self.content = content
    def edit(self):
        print("editing text document")

class WordDocument(TextDocument):
 def __init__(self, title, content, font_size):
  Document.__init__(self, title)  
  self.content = content
  self.font_size = font_size

word_doc = WordDocument("My Report", "This is the content", 12)

word_doc.whitespace()
word_doc.edit()



#Hierachial inheriatance
class MobileDevice:
 def __init__(self, brand):
  self.brand = brand

def turn_on(self):
  print(f"{self.brand} device turned on")

class Smartphone(MobileDevice):
  def __init__(self, brand, model):
   self.brand = brand  
   self.model = model

def make_call(self, number):
  print(f"Making a call to {number} from {self.brand} {self.model}")

class Tablet(MobileDevice):
  def __init__(self, brand, screen_size):
   self.brand = brand 
   self.screen_size = screen_size

def browse_internet(self):
  print(f"Browsing internet on {self.brand} {self.screen_size} inch tablet")

smartphone = Smartphone("Apple", "iPhone 14")
tablet = Tablet("Samsung", 11)

smartphone.turn_on()
smartphone.make_call("1234567890")
tablet.turn_on()
tablet.browse_internet()










#multiple inheritance
class Animal:
 def __init__(self, name):
  self.name = name

def make_sound(self):
  print("Animal makes a sound")

class Dog(Animal):
  def __init__(self, name, breed):
   self.name = name
   self.breed = breed

def make_sound(self):
  print(f"{self.name} ({self.breed}) barks")

dog = Dog("sheru", "maltipoo")
dog.make_sound()








#Hydrid inheritance

class birds:
   def __init__(self,name):
      self.name = name

      def fly(self):
         print(f"{self.name}  is flying")

class fish:
      def __init__(self,name):
       self.name = name

      def swim(self):
        print(f"{self.name} is swimming in water")

class Insect:
   def __init__(self, name):
       self.name = name

       def eat(self):
          print(f"{self.name} is eating")

birds = birds("parrot")       
fish = fish("star fish")
Insect = Insect("mosquite")


birds.fly()
fish.swim()
Insect.eat()

        
      

