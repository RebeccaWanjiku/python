# Object Oriented Programing

class Car:
            #constructor method
            def __init__(self,make,model,year):
                                    self.make=make
                                    self.model=model
                                    self.year=year
            #a method function
            def describe_car (self):
                    print(f"My dream car make: {self .make}," 
                                f"My dream car make: {self .model}, "
                                f"My dream car make: {self.year}, "
                          )
# create objects for instances of a class
myobj=Car("toyota", "lexus" ,2019)
myobj.describe_car()

class Manga:
    def __init__(self,name,author,status):
                            self.name=name
                            self.author=author
                            self.status=status
    def  research_manga(self):
                print(f"Manga: {self.name}. "
                            f"Written by: {self.author}.  "
                            f"The manga is: {self.status}. "
              )
myobj=Manga("Attack On Titan", "Yong Chi", "Completed")
myobj.research_manga()

class Movies:
    def __init__(self,jina,IMDB_rating ,Year):
                            self.jina=jina
                            self.IMDB_rating=IMDB_rating
                            self.Year=Year
    def  movies(self):
                print(f"Movie: {self.jina}. "
                            f"IMDB rating by: {self.IMDB_rating}.  "
                            f"Published on: {self.Year}. "
              )
myobj=Movies("The Fault In Our Stars", 6.7, 2021)
myobj.movies()

