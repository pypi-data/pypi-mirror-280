# 2. Abstract factory pattern

from abc import ABC, abstractstaticmethod

class Invalidexception(Exception):
    pass

class Readable(ABC):

    @abstractstaticmethod
    def showsubsidy():
        ...

    @abstractstaticmethod
    def tops():
        ...

class Book(Readable):
    def __init__(self):
        self.name = "You are now in book seciton"
    
    def tops(self):
        content = '''Naruto Uzumaki wants to be the best ninja in the land. 
He's done well so far, but with the looming danger posed by the mysterious Akatsuki organization, 
Naruto knows he must train harder than ever and leaves his village for intense exercises that will 
push him to his limits.'''
        print(content)
    
    def showsubsidy(self):
        print("The subscription amount of the book is Rs.500")

class Newspaper(Readable):
    def __init__(self):
        self.name = "You are now in newspaper section"

    def tops(self):
        content = '''1. Varisu trailer: Vijay's film is old wine in the most decorative bottle
2. Uttarakhand: Nepal villagers again pelt stones on Indian side
3. Another blunder': Sarfaraz Ahmed's stumping dismissal sparks huge debate during PAK vs NZ 2nd Test'''
        print(content)
    
    def showsubsidy(self):
        print("The subscription amount of the Newspaper is Rs.35")

class Magazine(Readable):
    def __init__(self):
        self.name = "You are now in magazine section"

    def tops(self):
        content = '''Filmfare is an Indian English-language fortnightly magazine published by Worldwide Media. 
Acknowledged as one of Indian most popular entertainment magazines, it publishes pieces involving news, 
interviews, photos, videos, reviews, events, and style.'''
        print(content)
    
    def showsubsidy(self):
        print("The subscription amount of the magazine is Rs.100")


class Readablefactory:

    @staticmethod
    def shop_objects(type):
        if type=="book":
            return Book()
        if type=="newspaper":
            return Newspaper()
        if type== "magazine":
            return Magazine()
        if choice=="exit":
            exit()
        else:
            raise Invalidexception("WRONG INPUT")

should_continue = True
while should_continue:
    choice = input("ENTER THE TYPE OF THE OBJECT: ").lower()
    shop=Readablefactory.shop_objects(choice)
    shop.tops()
    print("-----------------------------------------")




