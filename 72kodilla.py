class Person:
    def __init__(self, name, surname, email,telephone):
        self.name = name
        self.surname = surname
        self.email = email
        self.telephone= telephone

    def __str__(self):
        return f'{self.name} {self.surname}  {self.email} {self.telephone} '


Person1 = Person(name="Marta", surname="Luczak,",  email="m@wp.pl,",telephone= "+48 502224543")
Person2 = Person(name="Patryk", surname="Ziezio,",  email="d@wp.pl,",telephone=1)
Person3 = Person(name="Maciej", surname="Nowak,",  email="c@wp.pl,",telephone=1)
Person4 = Person(name="Edyta", surname="Las,", email="w@wp.pl,",telephone=1)
Person5 = Person(name="Maja", surname="Lisiecka,", email="e@wp.pl,",telephone=1)

items = [Person1, Person2, Person3, Person4, Person5]

for person in items:
    print(person)
print("________")

class Business(Person):
    def __init__ (self, company,position,email2, telephone2,name, surname, email,telephone):
        super().__init__(name, surname, email,telephone)
        self.company = company
        self.position = position
        self.email2=email2
        self.telephone2=telephone2

    def __str__(self):
        return f'{self.name} {self.surname}  {self.email2} {self.telephone2} {self.company} {self.position} '

    def contact(self):
        print(self.telephone)

#label_lenght
    def label_length(self):
        return(len(self.name + " " + self.surname))


business1=Business(name="Marta", surname="Luczak",  email="m@wp.pl",telephone=1,company="Citi",position="Analyst",email2=None, telephone2=None)
business2=Business(name="Patryk", surname="Ziezio",  email="d@wp.pl",telephone=1,company="HM",position="Analyst",email2=None, telephone2=None)
business3=Business(name="Maciej", surname="Nowak",  email="c@wp.pl",telephone=1,company="Zara",position="Analyst",email2=None, telephone2=None)
business4=Business(name="Edyta", surname="Las",  email="w@wp.pl",telephone=1,company="Sklep",position="Analyst",email2=None, telephone2=None)
business5=Business(name="Maja", surname="Lisiecka",  email="e@wp.pl",telephone=1,company="CCC",position="Analyst",email2=None, telephone2=None)


items2 = [business1,business2,business3,business4,business5]

for business in items2:
    print(business.contact())

from faker import Faker
fake = Faker()

#Stwórz klasę, która będzie przechowywać informacje z jednej wizytówki. Przyjmij, że każda wizytówka zawiera dane takie jak: imię,
# nazwisko, nazwa firmy, stanowisko, adres e-mail.


def generuj_wizytowki(rodzaj=visit_card, ilosc=1):
    wizytowki = []
    if rodzaj == visit_card:
        for i in range(0, ilosc):
            kontakt  = visit_card( imie=fake.name(), nazwisko=(""), telefon=fake.phone_number())
            wizytowki.append(kontakt)

    if rodzaj == Business:
        for i in range(0, ilosc):
            kontakt = Business(name=fake.name(), surname=(""), position=fake.job(), company=fake.company(),
                               telephone=fake.phone_number())
            wizytowki.append(kontakt)
    return wizytowki

wizytowki = generuj_wizytowki(Business, 5)
for i in wizytowki:
    print(i)