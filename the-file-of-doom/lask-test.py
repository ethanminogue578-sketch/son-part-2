from flask import Flask, render_template,request
import requests
app = Flask(__name__)


@app.route("/", methods=["GET","POST"])
def home():
    term = ""
    if request.method == "POST":
        term = request.form["search"]
    return render_template("index.html")
    

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/bookstore", methods=["GET","POST"])
def bookstore():
    term = ""
    if request.method == "POST":
        term = request.form["search"]
        return render_template("bookstore.html")
    # url = "https://openlibrary.org/search.json?q=dracula/&scrlybrkr=79698899"
    # response = requests.get(url, verify=False)
    # data = response.json()
    # books = data["docs"]
    # print(data)
    
    # for book in books:
        # print(book["title"])
    return render_template("bookstore.html")

@app.route("/bookstore/<title>")
def title(title):
    return render_template("book.html", title=title)

app.run(debug=True)