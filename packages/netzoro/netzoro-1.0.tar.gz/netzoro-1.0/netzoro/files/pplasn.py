#Iterator and comprehension patterns
class PplAsn:
    def __init__(self):
        self.lst=[]
        
    def __str__(self):
        return str(self.lst)

    def append(self,obj):
        self.lst.append(obj)

    def search(self,type,term):
        if type=="c":
            self.category_search(term)
        elif type=="n":
            self.name_search(term)

    def category_search(self,term):
        res=False
        for i in self.lst:
            if term in i.category:
                print(i)   
                res=True
        if not res:
            print("NO RESULTS FOUND!")

    def name_search(self,term):
        res=False
        for i in self.lst:
            if term in i.name:
                print(i)   
                res=True
        if not res:
            print("NO RESULTS FOUND!")
    
    def update_salary(self,role,inc):
        for i in self.lst:
            if i.category[0]==role:
                i.salary+=inc
    
    def add_fields(self,role,name,new):
        if role=="HOD" or role=="dean":
            for i in self.lst:
                if i.name==name:
                    i.category.append(new)
        else:
            raise ValueError("You are not a HOD or Dean! You can't add new fields!")
    
    def rem_fields(self,role,name,field):
        if role=="dean":
            for i in self.lst:
                if i.name==name:
                    i.category.remove(field)
        else:
            raise ValueError("You role can't remove fields!")
    
    def display(self):
        print("Here are all the records of people in this college:")
        for i in self.lst:
            print(i)
    
    
class Member:
    def __init__(self,name : str,age : int,category = str):
        self.name=name
        self.age=age
        self.category=category.split(",")

class Student(Member):
    def __init__(self,name,age,category,dept):
        super().__init__(name,age,category)
        self.dept=dept
        self.role= "Student"
    def __str__(self):
        return f"""Name: {self.name}
        Dept: {self.dept}
        Age: {self.age}
        Role" {self.role}
        Field Of Interest: {str(self.category)[1:-1]}
        ---------------------------------------------
        """

class Faculty(Member):
    def __init__(self,name,age,category,dept,salary,role="Faculty"):
        super().__init__(name,age,category)
        self.dept=dept
        self.role=role
        self.salary=salary
        def __str__(self):
            return f"""Name: {self.name}
            Dept: {self.dept}
            Age: {self.age}
            Role: {self.role}
            Field Of Interest: {str(self.category)[1:-1]}
            Salary: {self.salary}
            ---------------------------------------------
            """
    def __str__(self):
            return f"""Name: {self.name}
            Age: {self.age}
            Dept: {self.dept}
            Role: {self.role}
            Category: {str(self.category)[1:-1]}
            Salary: {self.salary}
            ---------------------------------------------
            """

class Staff(Member):
    def __init__(self,name,age,category,salary):
        super().__init__(name,age,category)
        self.role="Staff"
        self.salary=salary
        #since python already works with UTF-8, we don't have to explicity define anything to work with regional languages
    def __str__(self):
            return f"""Name: {self.name}
            Age: {self.age}
            Role: {self.role}
            Category: {str(self.category)[1:-1]}
            Salary: {self.salary}
            ---------------------------------------------
            """

pplasn=PplAsn()
s1=Student("Vedha",19,"ML,AI","IT")
s2=Student("Prasanth",20,"CyberSecurity,ML","ECE")
#s3=Student("Ravi Teja",19,"Ethical Hacking","IT")
#s4=Student("Mariappan",19,"ML,AI,DS","IT")
f1=Faculty("Joesph",40,"ML,AI","ECE",100000)
#f2=Faculty("Chandru",42,"Ethical Hacking,Cyber Security","IT",120000)
#f3=Faculty("Kavya",35,"DS,AI","IT",100000)
st1=Staff("कुमार",56,"Security",25000)

#appending
pplasn.append(s1)
pplasn.append(s2)
#pplasn.append(s3)
#pplasn.append(s4)
pplasn.append(f1)
#pplasn.append(f2)
#pplasn.append(f3)
pplasn.append(st1)

#searching
pplasn.search("c","Security")

#updating salaries
pplasn.update_salary("Security",2000)

print("After salary update: \n ")
#demonstrating update
pplasn.search("c","Security")

#demonstrating adding fields
print("Adding Fields:")
hod=Faculty("Ada",50,"AI,ML","IT",200000,"HOD")
print("Before: ")
#before
pplasn.name_search("Vedha")

#adding
pplasn.add_fields(hod.role,"Vedha","Cyber Security")
print("After:")
#after
pplasn.name_search("Vedha")

#demonstrating removing fields
print("Removing Fields")
dean=Faculty("Donuth",65,"AI,DS","ECE",250000,"dean")
print("Before: ")
#before
pplasn.name_search("Prasanth")

#removing
pplasn.rem_fields(dean.role,"Prasanth","CyberSecurity")
print("After:")
#after
pplasn.name_search("Prasanth")

#displaying all the data
pplasn.display()
