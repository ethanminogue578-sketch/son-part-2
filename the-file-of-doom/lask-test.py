from flask import Flask, render_template,request
import requests
import json
app = Flask(__name__)

try:
    with open("books.json") as f:
        books = json.load(f)
except FileNotFoundError:
    books = [{"title" : "Dracula", "author" : "Bram Stoker"},
{"title" : "The Hobbit", "author" : "JRR Tolkien"},
{"title" : "Don Quixote", "author" : "Miguel de Cervantes"},
]

def save_books():
    with open("books.json", "w") as f:
        json.dump(books, f)
    
@app.route("/", methods=["GET","POST"])
def home():

    return render_template("index.html")
    

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/bookstore", methods=["GET","POST"])
def bookstore():
    if request.method == "POST":
            books.append({"title" : request.form["title"],
                          "author" : request.form["author"]})
            save_books()
            print(books)
            return render_template("bookstore.html", books=books)
    # url = "https://openlibrary.org/search.json?q=dracula/&scrlybrkr=79698899"
    # response = requests.get(url, verify=False)
    # data = response.json()
    # books = data["docs"]
    # print(data)
    
    # for book in books:
        # print(book["title"])
    return render_template("bookstore.html", books=books)

@app.route("/bookstore/<title>")
def title(title):
    return render_template("book.html", title=title)

app.run(debug=True)