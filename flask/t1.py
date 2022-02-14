from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

headings = ("Name", "Role", "Salary")
data = (
  ("Rolf", "Software Engineer", "$42,000.00"),
  ("Ahmet", "Elektrikçi", "3,000.00")
  )
   
@app.route("/")
def home():
  return "Hello! this is the main page <h1>HELLO<h1>"

@app.route("/<name>")
def user(name):
  return f"Hellooo {name}!"

@app.route("/admin")
def admin():
  return redirect(url_for("user", name="Admin!"))

@app.route("/table")
def table():
    return render_template("table.html", headings=headings, data=data)

if __name__ == "__main__":
  app.run()

