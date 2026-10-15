import json

try:
    with open("books.json") as f:
        books = json.load(f)
except FileNotFoundError:
    books = []

class Book:
    def __init__(self, title, author, year, genre, stock):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self._stock = stock
    def restock(self, amount):
        self._stock = self._stock + amount
    def details(self):
        return (f"{self.title} is a {self.genre} book by {self.author} ({self.year})")
    def details_simple(self):
        return (f"{self.title} by {self.author} ({self.year})")
    def sell(self):
        if self._stock > 0:
            self._stock = self._stock - 1
        else:
            print("Sold out")
    def get_stock(self):
        return self._stock
    def set_stock(self, amount):
        if amount > 0:
            self._stock = amount
        else:
            print("Stock can't be negative")


# class Product:
   # def __init__ (self, title, price):
       # self.title = title
       # self.price = price
   # def label(self):
       # return f"{self.title} - £{self.price}"

# class Book(Product):
    # bdef __init__(self, title, price, author):
       # super().__init__(title, price)
       # self.author = author
    # def label(self):
        # return f"{self.title} by {self.author} - £{self.price}"

#  class Film(Product):
   # def __init__(self, title, price, director):
       # super().__init__(title, price)
        # self.director = director
    # def label(self):
        # return f"{self.title} by {self.director} - £{self.price}"

# class Game(Product):
   # def __init__(self, title, price, developer):
          #  super().__init__(title, price)
           # self.developer = developer
   # def label(self):
           # return f"{self.title} by {self.developer} - £{self.price}"

# def show_shelf(products):
    # for item in products:
       # print(item.label())

# mixed_shop = [Book("Don Quixote", 100, "Miguel de Cervantes"),
#               Film("The Matrix", 150, "Joel Silver"),
#               Game("Minecraft", 50, "Notch")]

# book_shop_2 =[
#     Book("The Little Red Book", 50, "Mao Zedong"),
#     Book("Watership Down", 70, "Richard Adams"),
#     Book("The Very Hungry Caterpillar", 200, "Eric Carle")
# ]

# show_shelf(mixed_shop)
# show_shelf(book_shop_2)


# b = Book("Dracula", 9, "Bram Stoker")
    
b1 = Book("The Hobbit", "JRR Tolkien", 1937, "Fantasy", 100)
b2 = Book("Goosebumps", "RL Stein", 1992, "Horror", 500)
b3 = Book("Journey to the West", "Wu Cheng'en", 1592, "Mythology", 10)
b4 = Book("And Then There Were None", "Agatha Christie", 1939, "Mystery", 5)
b5 = Book("Don Quixote", "Miguel de Cervantes", 1605, "Adventure", 3)

# book_shop =[
    # Book("The Little Red Book", "Mao Zedong", 1964, "Anthology", 67),
    # Book("Watership Down", "Richard Adams", 1972, "Adventure", 50),
    # Book("The Very Hungry Caterpillar", "Eric Carle", 1972, "Picture", 90)
# ]

# print(b1.title)
# print(b2.author)
# print(b1.details_simple())
# print(b2.details_simple())
# print(b1.details())
# print(b2.details())
# b4.restock(10)
# print(b4.stock)
# b5.sell()
# b5.sell()
# b5.sell()
# b5.sell()
# print(book_shop[0].title)
# book_shop[0].sell()
# print(book_shop[0].stock)
# for book in book_shop:
#     print(book.title, "-", book.stock)
#     book.sell()
#     print(book.title, "-", book.stock)
# print(b.title)
# print(b.price)
# print(b.author)
# print(json.dumps(books))
# for item in mixed_shop:
    # print(item.label())
    

b1.set_stock(-100)
print(b1.get_stock())