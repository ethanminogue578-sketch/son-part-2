class Book:
    def __init__(self, title, author, year, genre, stock):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.stock = stock
    def restock(self, amount):
        self.stock = self.stock + amount
    def details(self):
        return (f"{self.title} is a {self.genre} book by {self.author} ({self.year})")
    def details_simple(self):
        return (f"{self.title} by {self.author} ({self.year})")
    def sell(self):
        if self.stock > 0:
            self.stock = self.stock - 1
        else:
            print("Sold out")

class Product:
    def __init__ (self, title, price):
        self.title = title
        self.price = price
    def label(self):
        return f"{self.title} - £{self.price}"

class Book(Product):
    def __init__(self, title, price, author):
        super().__init__(title, price)
        self.artist = author
    def label(self):
        return f"{self.title} by {self.author} - £{self.price}"

# class Book2(Product):
    def __init__(self, title, price, author):
        super().__init__(title, price)
        self.author = author
    pass

b = Book("Dracula", 9, "Bram Stoker")
    
b1 = Book("The Hobbit", "JRR Tolkien", 1937, "Fantasy", 100)
b2 = Book("Goosebumps", "RL Stein", 1992, "Horror", 500)
b3 = Book("Journey to the West", "Wu Cheng'en", 1592, "Mythology", 10)
b4 = Book("And Then There Were None", "Agatha Christie", 1939, "Mystery", 5)
b5 = Book("Don Quixote", "Miguel de Cervantes", 1605, "Adventure", 3)

book_shop =[
    Book("The Little Red Book", "Mao Zedong", 1964, "Anthology", 67),
    Book("Watership Down", "Richard Adams", 1972, "Adventure", 50),
    Book("The Very Hungry Caterpillar", "Eric Carle", 1972, "Picture", 90)
]

print(b1.title)
print(b2.author)
print(b1.details_simple())
print(b2.details_simple())
print(b1.details())
print(b2.details())
b4.restock(10)
print(b4.stock)
b5.sell()
b5.sell()
b5.sell()
b5.sell()
print(book_shop[0].title)
book_shop[0].sell()
print(book_shop[0].stock)
for book in book_shop:
    print(book.title, "-", book.stock)
    book.sell()
    print(book.title, "-", book.stock)
print(b.title)
print(b.price)
print(b.author)
b.label