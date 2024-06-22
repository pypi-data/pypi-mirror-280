# 5. Template pattern

from abc import ABC, abstractmethod 

class College_admission(ABC):
    @abstractmethod
    def register(self):
        ...

    @abstractmethod
    def Submit_online_application(self):
        ...

    @abstractmethod
    def appear_interview(self):
        ...

    @abstractmethod
    def payment(slef):
        ...

    def process_admission(self):
        print("Preparing for admission")
        self.register()
        self.Submit_online_application()
        self.appear_interview()
        self.payment()
        print("Joined the college")


class Information_Technology(College_admission):

    def register(self):
        print("Go to www.ssnclg.com and click on admissons")

    def Submit_online_application(self):
        print("submit the appliation and it requires our passport size photo, aadhar card, birth certificate, choose your appropriate dept")

    def appear_interview(self):
        print("You have an aptitude test and a coding test")
    
    def payment(slef):
        print("Your fees will be 100000 per year and acc no : 3122215002311")


class Computer_science(College_admission):

    def register(self):
        print("Go to www.ssnclg.com and click on admissons")

    def Submit_online_application(self):
        print("submit the appliation and it requires our passport size photo, aadhar card, birth certificate, choose your appropriate dept")

    def appear_interview(self):
        print("You have an aptitude test and a coding test")
    
    def payment(slef):
        print("Your fees will be 150000 per year and acc no : 3122215002311")

class Mechanical_Engineering(College_admission):

    def register(self):
        print("Go to www.ssnclg.com and click on admissons")

    def Submit_online_application(self):
        print("submit the appliation and it requires our passport size photo, aadhar card, birth certificate, choose your appropriate dept")

    def appear_interview(self):
        print("You have an aptitude test")
    
    def payment(slef):
        print("Your fees will be 120000 per year and acc no : 3122215002311")

choice = input("What type of cake you want? (IT || CS || ME)")
if choice == 'IT':
    o=Information_Technology()
    o.process_admission()
elif choice == 'CS':
    o=Computer_science()
    o.process_admission()
elif choice == 'ME':
    o=Mechanical_Engineering()
    o.process_admission()
else:
    print("NO ADDMISSION")
    
