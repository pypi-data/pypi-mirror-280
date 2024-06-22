from collections import deque

class Employee:
  def __init__(cls,name,des):
    cls.name=name
    cls.des=des

class System:
  def __init__(cls,name,specs):
    cls.name=name
    cls.des=specs

class PrintJob:

  __instance = []
  __queue = deque()

  def __new__(cls,emp,empid):
    cls.emp=emp
    cls.empid=empid
    if (cls.__instance is None):

      cls.__instance = super(PrintJob,cls).__new__(cls)
    
    PrintJob.__queue.append(emp)
    return cls
  
  @staticmethod
  def printjobs():
    for i in PrintJob.__queue:
      print("Name: ",i.name)
      print("Description: ",i.des)

  @staticmethod
  def Deleteprint():
    PrintJob.__queue.popleft()

EmployeeX=Employee("Raghul","software")
EmployeeY=Employee("Prasanth","hardware")

systemA=System("Hp","i7")
systemB=System("Lenovo","i5")

p1=PrintJob(EmployeeX,123)
p2=PrintJob(EmployeeY,143)

s1=PrintJob(systemA,542)
s2=PrintJob(systemB,976)
print("Same id ---{}-{}".format(id(p1),id(p2)))
print("Before deleting:")

p1.printjobs()
print("--------------------------------------")
print("After deleting:")
p1.Deleteprint()

p1.printjobs()
print("--------------------------------------")