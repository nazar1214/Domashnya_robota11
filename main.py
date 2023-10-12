class film:
    chis=0
    def __init__(self, name, date, creators, time):
        self.name = name
        self.date = date
        self.creators = creators
        self.time = time
        film.chis+= 1

    def set_name(self, name):
        self.name = name

    def set_date(self, date):
        self.date = date

    def set_creators(self, creators):
        self.creators = creators

    def set_time(self, time):
        self.time = time

    def get_name(self):
        return self.name

    def get_date(self):
        return self.date

    def get_creators(self):
        return self.creators

    def get_time(self):
        return self.time

class dorichifilm(film):
    def __init__(self, name, date, creators, time, shanr):
        film.__init__(self, name, date, creators, time)
        self.shanr = shanr



dorfilm = dorichifilm("not breaking bad", "1111", "walter ginger", "1 minute", "drama")
my_film1 = film("breaking bad", 2025, "walter white", "1:30 Hours")
my_film9 = film("breaking good", 2004, "walter bread", "30 Hours")


my_film1.set_name("breaking in house")
my_film1.set_date("20220")
my_film1.set_creators("walter sigma")
my_film1.set_time("2 hours")

print(film.chis)

print(dorfilm.get_name()) 
print(dorfilm.get_date()) 
print(dorfilm.get_creators())  
print(dorfilm.get_time()) 