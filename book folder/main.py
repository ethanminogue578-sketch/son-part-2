class Book:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
    def details(self):
        return (f"{self.title} is a {self.genre} book by {self.author} ({self.year})")
    def details_simple(self):
        return (f"{self.title} by {self.author} ({self.year})")
    
b1 = Book("The Hobbit", "JRR Tolkien", 1937, "Fantasy")
b2 = Book("Goosebumps", "RL Stein", 1992, "Horror")
b3 = Book("Journey to the West" "Wu Cheng'en", 1592, "Mythology")

print(b1.title)
print(b2.author)
print(b1.details_simple())
print(b2.details_simple())

        

