class Person():
    def __init__(self,name):
        self.name=name
    def update(self,msg):
        print("Message for",self.name,":",msg)
class Grandparents():
    def __init__(self,children):
        self.chidren=children
class Son1():
    def __init__(self,wife,children):
        self.wife=wife
        self.children=children
class Son2():
    def __init__(self,wife,children):
        self.wife=wife
        self.children=children
class Joint_Family():
    def __init__(self,members):
        self.members=members
    def send_message(self,msg):
        print("Joint Family Group")
        for i in self.members:
            i.update(msg)
    def exit_group(self,name):
        count=0
        for i in self.members:
            if i.name==name:
                c=i
                break
            else:
                count+=1
        if count==len(self.members):
            print("You are not a part of this group")
        else:
            self.members.remove(c)
            for i in self.members:
                st=c.name+" "+"has left the group"
                i.update(st)
class Son1_Family():
    def __init__(self,members):
        self.members=members
    def send_message(self,msg):
        print("Son1_Family group")
        for i in self.members:
            i.update(msg)
    def exit_group(self,name):
        count=0
        for i in self.members:
            if i.name==name:
                c=i
                break
            else:
                count+=1
        if count==len(self.members):
            print("You are not a part of this group")
        else:
            self.members.remove(c)
            for i in self.members:
                st=c.name+" "+"has left the group"
                i.update(st)
class Son2_Family():
    def __init__(self,members):
        self.members=members
    def send_message(self,msg):
      print("Son2_Family group")
      for i in self.members:
            i.update(msg)
    def exit_group(self,name):
        count=0
        for i in self.members:
            if i.name==name:
                c=i
                break
            else:
                count+=1
        if count==len(self.members):
            print("You are not a part of this group")
        else:
            self.members.remove(c)
            for i in self.members:
                st=c.name+" "+"has left the group"
                i.update(st)
class Young():
    def __init__(self,members):
        self.members=members
    def send_message(self,msg):
        print("Young Family group")
        for i in self.members:
            i.update(msg)
    def exit_group(self,name):
        count=0
        for i in self.members:
            if i.name==name:
                c=i
                break
            else:
                count+=1
        if count==len(self.members):
            print("You are not a part of this group")
        else:
            self.members.remove(c)
            for i in self.members:
                st=c.name+" "+"has left the group"
                i.update(st)
grandparent1=Person("Srinivas")
grandparent2=Person("Lalitha")
son1=Person("Ashok")
son2=Person("Abhay")
p5=Grandparents([son1,son2])
wife1=Person("Madhavi")
daughter1=Person("Jahnvi")
po2=Son1(wife1,[daughter1])
wife2=Person("Bindu")
daughter2=Person("Satya")
son_2=Person("Jagadeesh")
p=Son2(wife2,[daughter2,son_2])
joint_group=Joint_Family([grandparent1,grandparent2,son1,son2,wife1,daughter1,wife2,daughter2,son_2])
son1_group=Son1_Family([son1,wife1,daughter1])
son2_group=Son2_Family([son2,wife2,daughter2,son_2])
young_group=Young([daughter1,daughter2,son_2])
n=int(input("enter how many operations you would like to make"))
for i in range(n):
 print("1.Message to Joint group,2.Message to specific group,3.Leave group")
 ch=int(input("enter any choice"))
 if ch==1:
    msg=input("enter any msg")
    joint_group.send_message(msg)
 elif ch==2:
    print("Which group do you want to send message to")
    print("1.Son1_Family,2.Son2_Family,3.Young_Family")
    ch=int(input("enter any choice"))
    if ch==1:
        msg=input("enter any message")
        son1_group.send_message(msg)
    elif ch==2:
        msg=input("enter any message")
        son2_group.send_message(msg)
    else:
        msg=input("enter any message")
        young_group.send_message(msg)
 else:
    name=input("enter name")
    print("1.Leave Joint Family Group,2.Son1_family group,3.Son2_Family group,4.Young Family group")
    ch=int(input("enter which group you want to leave"))
    if ch==1:
        joint_group.exit_group(name)
    elif ch==2:
        son1_group.exit_group(name)
    elif ch==3:
        son2_group.exit_group(name)
    elif ch==4:
        young_group.exit_group(name)
    else:
        print("invalid choice")
