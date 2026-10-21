from flask import Flask, render_template,request,flash,session,redirect,url_for
from werkzeug.security import generate_password_hash, check_password_hash
import requests
import json
app = Flask(__name__)
app.secret_key = "change-this"

users = {
    "staff": generate_password_hash("bookworm")
}


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
    if request.method == "POST":
        if "user" not in session:
            flash("Please log in to add books")
            return redirect(url_for("login"))
        session["name"] = request.form["name"]
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/bookstore", methods=["GET","POST"])
def bookstore():
    if request.method == "POST":

            title = request.form["title"]
            author = request.form["author"]
            
            if title and author:
                books.append({"title" : request.form["title"],
                          "author" : request.form["author"]})
                flash("Book has been added.")
                save_books()
                print(books)
            else:
                flash("Fill in both fields before adding a book.")
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

@app.route("/cart")
def cart():
    return render_template(cart.html, "cart", [])

@app.route("/empty")
def empty():
    session["cart"] = []

@app.route("/app/<title>")
def add(title):
    cart = session.get("cart", [])
    cart.append(title)
    session["cart"] = cart
    return redirect(url_for("home"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form["username"]
        pw   = request.form["password"]
        if name in users and check_password_hash(users[name], pw):
            session["user"] = name
            return redirect(url_for("home"))
        flash("Wrong username or password")
    return render_template("login.html")

@app.route("/logout", methods=["GET", "POST"])
def logout():
    session.pop("user", None)
    return redirect(url_for("home"))

app.run(debug=True)