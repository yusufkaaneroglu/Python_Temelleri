# class
class Person:
    
    # class attributes
    address = 'no information'
    # constructor (yapıcı method)
    def __init__(self, name, year):
        # object attributes
        self.name = name 
        self.year = year
        print('init metodu çalıştır.')

        #  methods
        def intro(self):
            print('Hello There. I am '+ self.name)

# object (instance)
p1 = Person('Yusuf', 2000)
p2 = Person('Yağmur', 1995)

p1.intro()
