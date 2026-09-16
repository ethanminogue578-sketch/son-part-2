from flask import Flask, render_template,request
app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
    term = ""
    if request.method == "POST":
        term = request.form["search"]
    return render_template("albumstore.html")
    

@app.route("/about")
def about():
    return "We are the record(store) and we make records"

@app.route("/album")
def album():
    albums = {"Kind of Blue", "Rumours", "Thriller"}
    return render_template("albumstore.html", albums=albums)

@app.errorhandler(404)
def not_found(erorr):
    return render_template("404.html"), 404

app.run(debug=True)