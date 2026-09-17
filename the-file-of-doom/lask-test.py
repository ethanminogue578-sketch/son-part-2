from flask import Flask, render_template,request
app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
    term = ""
    if request.method == "POST":
        term = request.form["search"]
    return render_template("Index.html")
    

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/album", methods=["GET","POST"])
def album():
    term = ""
    if request.method == "POST":
        term = request.form["search"]
        return render_template("albumstore.html")
    albums = {"Kind of Blue", "Rumours", "Thriller"}
    return render_template("albumstore.html", albums=albums)

@app.route("/album/<title>")
def title(title):
    return render_template("album.html", title=title)

@app.errorhandler(404)
def not_found(erorr):
    return render_template("404.html"), 404

app.run(debug=True)