#Object IntroSpection in Python

class Employee:

    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        #self.email = f"{fname}.{lname}@codewithharry.com"

    def explain(self):
        return f"This Employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname==None or self.lname == None:
            return "Email is not set.please set it using setter"
        return f"{self.fname}.{self.lname}@codewithharry.com"

    @email.setter
    def email(Self,string):
        print("Setting now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None   

skillf = Employee('Skill','f')
print(skillf.email)

#Object Introspection  is method to get information about object

print(type(skillf))
print(type("This is a string"))
print(id("This is a string")) #Object unique id
print(type("that that"))

o = 'This is a string' 
#it will give all information about functioni
print(dir(o))
print(dir(skillf))


#inspect Module
import inspect
print(inspect.getmembers(skillf))


# hindustani_supporter = Employee('Hindustani','Supporter')
# #nikil_raj_pandey = Employee("Nikhi","Raj")
# # 
# hindustani_supporter.fname = 'US'

# print(hindustani_supporter.email)
# hindustani_supporter.email = 'this.that@codewithharry.com'
# print(hindustani_supporter.fname)
