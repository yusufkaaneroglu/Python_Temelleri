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

        # methods
    

# object (instance)
p1 = Person(name ='Yusuf', year =2000)
p2 = Person(name ='Yağmur', year =1995)

#updating
p1.name='Ahmet'
p1.address='Konya'

# accessing object attributes
print(f'p1 :name: {p1.name} year: {p1.year} address: {p1.address}')
print(f'p2 :name: {p2.name} year: {p2.year} address: {p2.address}')

print(type(p1))
print(type(p2))
print(p1 == p2)
