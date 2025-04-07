from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    # return("<h2>This is About Page</h2>")
    return render_template("about.html")


@app.route("/contact")
def contact():   
    # return("<h3>This is contact page</h3>") 
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
