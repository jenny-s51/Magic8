from flask import Flask, render_template
import random
app = Flask(__name__)

# Defining the home page of our site
@app.route("/")  # this sets the route to this page
def home():
    return render_template("magic8.html")

@app.route("/swanson.html")
def swanson():
    return render_template("swanson.html")

@app.route("/yesno.html")
def yesno():
    return render_template("yesno.html")

@app.route("/shakespeare.html")
def shakespeare():
    return render_template("shakespeare.html")

def answer(filename):
    f = open(filename, "r")
    answers = f.readlines() #Turns the file into a list of lines, each containing a different answer
    print(random.sample(answers, 1)[0])
 
if __name__ == "__main__":
    app.run()