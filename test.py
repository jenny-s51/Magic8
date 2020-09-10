from flask import Flask, render_template
import random, requests
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
    return random.sample(answers, 1)[0].strip("\n") #Pick a random selection and return it to html
 
def yes_no_answer(): #Easy yes or no answer
    return random.choice(["Yes", "No"])

def swanson_answer(): #Query the Ron Swanson quotes API
    response = requests.get("http://ron-swanson-quotes.herokuapp.com/v2/quotes")
    if response.status_code == 200:
        return response.json()[0]
    else:
        return "Something went wrong with Swanson API..."

if __name__ == "__main__":
    #print(answer("regular_answers"))
    #print(answer("shakespeare_answers"))
    #print(yes_no_answer())
    #print(swanson_answer())

    app.run()