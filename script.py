class Person: # declare the class
    """Represents a Person with pets
       attributes: first_name, last_name,
                   age, pets
    """

alice = Person() #instantiate the object

#assign values to attributes
alice.first_name = "Alice"
alice.last_name = "Smith"
alice.age = 22
alice.pets = ["fido", "rover"] #can be any type

#access attributes
print(alice.first_name) #=> "Alice"
print(alice.last_name) #=> "Smith"
print(alice.pets[1]) #=> "rover"

bob = Person()
bob.first_name = "Bob"
bob.last_name = "Brown"

print(bob.first_name)
